import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_DB = BASE_DIR / "data" / "populacao.db"


def main():
    print("🗄️ Conectando ao banco SQLite...")

    conn = sqlite3.connect(CAMINHO_DB)

    query = "SELECT * FROM populacao"

    df = pd.read_sql_query(query, conn)

    print("\n📊 Dados do banco:")
    print(df.to_string(index=False))

    conn.close()
    print("\n✅ Conexão encerrada.")


if __name__ == "__main__":
    main()

    import sqlite3

BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_DB = BASE_DIR / "data" / "populacao.db"


def main():
    conn = sqlite3.connect(CAMINHO_DB)

    query = """
    SELECT *
    FROM populacao
    ORDER BY ano, municipio
    """

    df = pd.read_sql_query(query, conn)

    print(df)

    conn.close()


if __name__ == "__main__":
    main()
