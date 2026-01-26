import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_ENTRADA = BASE_DIR / "data" / "raw" / "populacao_ibge_raw.csv"
CAMINHO_SAIDA = BASE_DIR / "data" / "processed" / "populacao_ibge_tratada.csv"

def main():
    df = pd.read_csv(
        CAMINHO_ENTRADA,
        sep=";",
        encoding="latin1",
        on_bad_lines="skip"
    )

    df.to_csv(CAMINHO_SAIDA, index=False)
    print("✅ Extract concluído!")

if __name__ == "__main__":
    main()
