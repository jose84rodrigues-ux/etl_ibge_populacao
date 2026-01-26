import pandas as pd
from pathlib import Path

# Caminhos do projeto
BASE_DIR = Path(__file__).resolve().parent.parent
CAMINHO_RAW = BASE_DIR / "data" / "raw" / "populacao_ibge_raw.csv"
CAMINHO_PROCESSED = BASE_DIR / "data" / "processed" / "populacao_tratada.csv"


def main():
    print("🚀 Iniciando transformação dos dados...")

    # Leitura do CSV bruto (tolerante a erros)
    df = pd.read_csv(
        CAMINHO_RAW,
        sep=",",
        encoding="utf-8",
        engine="python",
        on_bad_lines="skip"
    )

    print(f"📥 Registros recebidos: {df.shape[0]}")
    print("📋 Colunas detectadas:")
    print(df.columns.tolist())

    # Padroniza nomes das colunas
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    # Ajuste do nome da coluna de população (segurança)
    if "populacao_residente" in df.columns:
        df = df.rename(columns={"populacao_residente": "populacao"})

    # Seleção final
    df = df[["ano", "populacao"]]

    # Garante que a pasta processed existe
    CAMINHO_PROCESSED.parent.mkdir(parents=True, exist_ok=True)

    # Salva CSV tratado
    df.to_csv(
        CAMINHO_PROCESSED,
        index=False,
        sep=";",
        encoding="utf-8"
    )

    print("✅ Transformação concluída com sucesso")
    print(f"💾 Arquivo salvo em: {CAMINHO_PROCESSED}")


if __name__ == "__main__":
    main()
