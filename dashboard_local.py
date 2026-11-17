"""Prototipo de dashboard local (HTTP Basic), acceso restringido por rol."""
import os, base64, hmac, html
from pathlib import Path
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import pandas as pd

BASE = Path(__file__).resolve().parent
USERS = {
 "ADMIN": os.environ.get("DATAPULSE_ADMIN_PASSWORD", ""),
 "CAJAMARCA": os.environ.get("DATAPULSE_CAJAMARCA_PASSWORD", "")
}
if not all(USERS.values()) or USERS["ADMIN"] == USERS["CAJAMARCA"]:
    raise SystemExit("Establezca contraseñas distintas en DATAPULSE_ADMIN_PASSWORD y DATAPULSE_CAJAMARCA_PASSWORD")

def authenticate(header):
    try:
        user, password = base64.b64decode(header.split(" ", 1)[1], validate=True).decode().split(":", 1)
        if user in USERS and hmac.compare_digest(password, USERS[user]):
            return user
    except (ValueError, IndexError, UnicodeDecodeError, AttributeError, TypeError):
        pass
    return None

def barras(series, titulo):
    counts = series.head(10)
    if counts.empty:
        return "<p>Sin datos</p>"
    biggest = max(counts.max(), 1)
    body = "".join(f"<p>{html.escape(str(k))}: <b>{int(v)}</b></p><div style='height:10px;background:#dfebf0'><div style='height:10px;width:{int(100*v/biggest)}%;background:#2080a0'></div></div>" for k,v in counts.items())
    return f"<section><h3>{html.escape(titulo)}</h3>{body}</section>"

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        role = authenticate(self.headers.get("Authorization"))
        if not role:
            self.send_response(401)
            self.send_header("WWW-Authenticate", 'Basic realm="DataPulse local"')
            self.end_headers()
            return
        df = pd.read_csv(BASE / "datos" / "dataset_limpio.csv", sep=";", encoding="utf-8-sig", parse_dates=["FECHA"])
        # Restringir filas ANTES de calcular los indicadores.
        if role == "CAJAMARCA":
            df = df.loc[df.DEPARTAMENTO == "CAJAMARCA"].copy()
        query = parse_qs(urlparse(self.path).query)
        allowed = sorted(df.DEPARTAMENTO.dropna().unique())
        department = query.get("departamento", ["TODOS"])[0]
        year = query.get("anio", ["TODOS"])[0]
        if department in allowed:
            df = df.loc[df.DEPARTAMENTO == department]
        if year in ("2020", "2021"):
            df = df.loc[df.FECHA.dt.year == int(year)]
        n = len(df)
        fatal = int(df.FALLECIDOS.gt(0).sum())
        valid = int(df.FALLECIDOS.notna().sum())
        rate = 100*fatal/valid if valid else 0
        options = '<option value="TODOS">Todos los permitidos</option>' + "".join(f'<option value="{html.escape(s,quote=True)}">{html.escape(s)}</option>' for s in allowed)
        style = "<style>body{font:16px Arial;max-width:1100px;margin:30px auto;background:#f4f7fa;color:#12304b}header{background:#174a6b;color:white;padding:20px}section{background:white;border-radius:9px;padding:18px;margin:12px}main{display:grid;grid-template-columns:1fr 1fr}select,button{padding:9px}</style>"
        page = f"""<!doctype html><html lang="es"><meta charset="utf-8">{style}
<header><h1>DataPulse Ingeniería — SUTRAN</h1><p>Rol: {role} | Prototipo local</p></header>
<form><label>Departamento <select name="departamento">{options}</select></label>
<label>Año <select name="anio"><option>TODOS</option><option>2020</option><option>2021</option></select></label><button>Filtrar</button></form>
<section><strong>Accidentes: {n}</strong> | Con fallecidos: {fatal} | Porcentaje sobre registros conocidos: {rate:.2f}%</section>
<main>
{barras(df.DEPARTAMENTO.fillna("NO INFORMADO").value_counts(),"Accidentes por departamento")}
{barras(df.MODALIDAD.fillna("NO INFORMADO").value_counts(),"Modalidad")}
{barras(df.groupby(df.FECHA.dt.strftime("%Y-%m")).size().sort_index(),"Registros por mes")}
{barras(df.HERIDOS.fillna(-1).clip(upper=10).map(lambda v:"SIN DATO" if v<0 else ("10+" if v>=10 else str(int(v)))).value_counts(),"Heridos por accidente")}
</main><p>Los conteos no equivalen a tasas de riesgo vial. Uso académico local.</p></html>"""
        encoded = page.encode("utf-8")
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(encoded)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(encoded)

if __name__ == "__main__":
    print("Abra http://127.0.0.1:8765")
    HTTPServer(("127.0.0.1", 8765), Handler).serve_forever()
