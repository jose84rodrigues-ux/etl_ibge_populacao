import pandas as pd
import sqlite3
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_CSV = BASE_DIR / "data" / "processed" / "populacao_tratada.csv"
CAMINHO_DB = BASE_DIR / "database" / "populacao.db"


def main():
    # 1. Ler CSV tratado
    df = pd.read_csv(CAMINHO_CSV)

    # 2. Conectar ao SQLite
    conn = sqlite3.connect(CAMINHO_DB)

    # 3. Carregar dados no banco
    df.to_sql(
        name="populacao_ibge",
        con=conn,
        if_exists="replace",
        index=False
    )

    # 4. Validação simples
    total = pd.read_sql(
        "SELECT COUNT(*) AS total_registros FROM populacao_ibge",
        conn
    )

    conn.close()

    print("✅ Load concluído com sucesso!")
    print(f"📊 Total de registros carregados: {total.iloc[0,0]}")


if __name__ == "__main__":
    main()
