import pandas as pd
from pathlib import Path

# Diretórios base
BASE_DIR = Path(__file__).resolve().parent.parent

CAMINHO_RAW_ENTRADA = BASE_DIR / "data" / "raw" / "populacao_ibge_raw.csv"
CAMINHO_RAW_SAIDA   = BASE_DIR / "data" / "raw" / "populacao_ibge_extracted.csv"


def main():
    print("🔍 Lendo dados brutos...")

    df = pd.read_csv(
        CAMINHO_RAW_ENTRADA,
        sep=";",
        encoding="latin1",
        engine="python"
    )

    print(f"📥 Registros lidos: {df.shape[0]}")

    # Salvando saída do extract
    df.to_csv(
        CAMINHO_RAW_SAIDA,
        index=False,
        encoding="utf-8-sig"
    )

    print(f"✅ Extract concluído! Arquivo salvo em:\n{CAMINHO_RAW_SAIDA}")


if __name__ == "__main__":
    main()
