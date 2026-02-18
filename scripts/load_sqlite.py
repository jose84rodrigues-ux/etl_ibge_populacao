import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_PROCESSED = BASE_DIR / "data" / "processed" / "populacao_tratada.csv"
CAMINHO_DB = BASE_DIR / "data" / "populacao.db"


def main():
    print("🔄 Carregando dados tratados no SQLite...")

    df = pd.read_csv(CAMINHO_PROCESSED)

    conn = sqlite3.connect(CAMINHO_DB)

    df.to_sql("populacao", conn, if_exists="replace", index=False)

    conn.close()

    print("✅ Dados carregados com sucesso!")
    print("📊 Total inserido:", len(df))


if __name__ == "__main__":
    main()
