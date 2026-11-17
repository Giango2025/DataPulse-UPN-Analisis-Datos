"""DataPulse: ingesta y análisis de accidentes SUTRAN (pasos 1 a 5)."""
from pathlib import Path
import sqlite3
import numpy as np
import pandas as pd
from scipy import stats
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

BASE = Path(__file__).resolve().parent
SRC = BASE / "datos" / "dataset_fuente.csv"
OUT = BASE / "datos" / "dataset_limpio.csv"

def ejecutar():
    if not SRC.exists():
        raise FileNotFoundError("Coloque una copia autorizada del CSV en datos/dataset_fuente.csv")
    raw = pd.read_csv(SRC, sep=";", encoding="latin-1", dtype={"CODIGO_VÍA": "string"})
    print("Registros originales:", len(raw), "Columnas:", len(raw.columns))
    print("Nulos (%):", raw.isna().mean().mul(100).round(2).to_dict())
    print("Duplicados:", int(raw.duplicated().sum()))
    df = raw.replace(r"^\s*(N\.I\.|)$", np.nan, regex=True).drop_duplicates().copy()
    for c in ["DEPARTAMENTO", "CODIGO_VÍA", "MODALIDAD"]:
        df[c] = df[c].astype("string").str.strip().str.upper().replace("", pd.NA)
    for c in ["FECHA", "FECHA_CORTE"]:
        df[c] = pd.to_datetime(df[c], dayfirst=True, errors="coerce")
    for c in ["KILOMETRO", "FALLECIDOS", "HERIDOS"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")
        df.loc[df[c] < 0, c] = np.nan
    df["AÑO"] = df.FECHA.dt.year.astype("Int64")
    df["MES"] = df.FECHA.dt.month.astype("Int64")
    df["TOTAL_VICTIMAS"] = df.FALLECIDOS + df.HERIDOS
    df["EVENTO_FATAL"] = np.where(df.FALLECIDOS.notna(), (df.FALLECIDOS > 0).astype(int), np.nan)
    if df.FECHA.isna().any():
        raise ValueError("Hay fechas inválidas; revisar la fuente antes de analizar")
    OUT.parent.mkdir(exist_ok=True, parents=True)
    df.to_csv(OUT, sep=";", index=False, encoding="utf-8-sig", date_format="%Y-%m-%d")
    with sqlite3.connect(BASE / "sutran_analisis.sqlite") as con:
        sql_df = df.copy()
        for c in ["FECHA", "FECHA_CORTE"]:
            sql_df[c] = sql_df[c].dt.strftime("%Y-%m-%d")
        sql_df.to_sql("accidentes_limpios", con, index=False, if_exists="replace")
        con.executescript((BASE / "analisis_corregido.sql").read_text(encoding="utf-8"))
    fatal = df.EVENTO_FATAL.dropna().astype(int)
    p, n = float(fatal.mean()), len(fatal)
    err = 1.96 * np.sqrt(p * (1-p) / n)
    print("Registros limpios:", len(df), "Eventos fatales:", int(fatal.sum()))
    print("Porcentaje con fallecidos:", round(100*p, 2), "IC95%:", round(100*(p-err),2), round(100*(p+err),2))
    print("Estadísticas:", df[["KILOMETRO", "FALLECIDOS", "HERIDOS"]].describe().to_string())
    tab = pd.crosstab(df.loc[df.EVENTO_FATAL.notna(), "DEPARTAMENTO"].fillna("NO INFORMADO"), fatal)
    print("Prueba chi-cuadrado p:", stats.chi2_contingency(tab).pvalue)
    dept = df.DEPARTAMENTO.fillna("NO INFORMADO").value_counts()
    meses = df.groupby(df.FECHA.dt.to_period("M")).size().sort_index()
    figs = BASE / "visualizaciones"
    figs.mkdir(exist_ok=True)
    fig, ax = plt.subplots(figsize=(8, 4))
    ax.hist(df.HERIDOS.dropna(), bins=range(0,21), edgecolor="black")
    ax.set(xlabel="Heridos por accidente (0-19)", ylabel="Frecuencia", title="Distribución de heridos (eventos >=20 fuera del encuadre)")
    fig.tight_layout(); fig.savefig(figs / "viz_01_histograma.png"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(8,4))
    ax.boxplot(df.HERIDOS.dropna(), vert=False, showfliers=True)
    ax.set(xlabel="Heridos por accidente", title="Valores atípicos observados")
    fig.tight_layout(); fig.savefig(figs / "viz_02_boxplot.png"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(8,4))
    dept.head(10).sort_values().plot.barh(ax=ax)
    ax.set(xlabel="Accidentes registrados", ylabel="Departamento", title="Departamentos con más registros")
    fig.tight_layout(); fig.savefig(figs / "viz_03_barras.png"); plt.close(fig)
    fig, ax = plt.subplots(figsize=(9,4))
    ax.plot(meses.index.astype(str), meses.values, marker="o")
    ax.tick_params(axis="x", rotation=70)
    ax.set(xlabel="Mes", ylabel="Registros", title="Registros mensuales 2020–2021")
    fig.tight_layout(); fig.savefig(figs / "viz_04_serie_temporal.png"); plt.close(fig)
    return df

if __name__ == "__main__":
    ejecutar()
