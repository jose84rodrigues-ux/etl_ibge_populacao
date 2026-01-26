import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_INPUT = BASE_DIR / "data" / "processed" / "populacao_ibge_tratada.csv"
CAMINHO_OUTPUT = BASE_DIR / "data" / "processed" / "populacao_ibge_tratada.csv"

def main():
    df = pd.read_csv(CAMINHO_INPUT)

    df.columns = [c.lower().strip().replace(" ", "_") for c in df.columns]
    df.drop_duplicates(inplace=True)

    df.to_csv(CAMINHO_OUTPUT, index=False)
    print("✅ Transform concluído!")

if __name__ == "__main__":
    main()
