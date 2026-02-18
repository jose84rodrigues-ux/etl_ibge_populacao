import sys
import pandas as pd
from pathlib import Path

# Garantir exibição correta no terminal
sys.stdout.reconfigure(encoding='utf-8')

print("📥 Lendo arquivo raw...")

# Caminhos organizados
BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_RAW = BASE_DIR / "data" / "raw" / "populacao_ibge_raw.csv"
CAMINHO_PROCESSED = BASE_DIR / "data" / "processed" / "populacao_tratada.csv"

# Ler arquivo raw
df = pd.read_csv(
    CAMINHO_RAW,
    sep=",",
    encoding="utf-8-sig",
    on_bad_lines="skip"
)

# Garantir colunas esperadas
colunas_esperadas = [
    "ano",
    "cod_uf",
    "uf",
    "cod_municipio",
    "municipio",
    "regiao",
    "populacao"
]

df = df[colunas_esperadas]

# Corrigir tipos de dados
# Garantir que "ano" seja numérico (linhas inválidas viram NaN)
df["ano"] = pd.to_numeric(df["ano"], errors="coerce")

# Remover linhas onde ano é inválido
df = df.dropna(subset=["ano"])

# Agora sim converter para inteiro
df["ano"] = df["ano"].astype(int)

# Converter demais colunas
df["cod_uf"] = pd.to_numeric(df["cod_uf"], errors="coerce").astype("Int64")
df["cod_municipio"] = pd.to_numeric(
    df["cod_municipio"], errors="coerce").astype("Int64")
df["populacao"] = pd.to_numeric(
    df["populacao"], errors="coerce").astype("Int64")


# Criar pasta processed se não existir
CAMINHO_PROCESSED.parent.mkdir(parents=True, exist_ok=True)

# Salvar CSV tratado
df.to_csv(
    CAMINHO_PROCESSED,
    index=False,
    encoding="utf-8"
)

print("✅ Arquivo tratado salvo com sucesso!")
print("📂 Local:", CAMINHO_PROCESSED)
print("📊 Total de registros:", len(df))
