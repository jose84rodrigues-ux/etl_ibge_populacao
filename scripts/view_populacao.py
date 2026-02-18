import pandas as pd
from pathlib import Path

# Caminho base
BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_PROCESSED = BASE_DIR / "data" / "processed" / "populacao_tratada.csv"


def main():
    print("📊 Carregando dados tratados...")

    df = pd.read_csv(
        CAMINHO_PROCESSED,
        sep=";",
        encoding="utf-8"
    )

    print("\n📋 Tabela formatada:")
    print(df.to_string(index=False))

    print("\n📐 Informações gerais:")
    print(df.info())


if __name__ == "__main__":
    main()
