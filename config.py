import os

CAMINHO_ENV = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".env")


def _carregar_dotenv(caminho: str) -> None:
    if not os.path.isfile(caminho):
        return
    with open(caminho, encoding="utf-8") as arquivo:
        for linha in arquivo:
            linha = linha.strip()
            if not linha or linha.startswith("#") or "=" not in linha:
                continue
            chave, valor = linha.split("=", 1)
            chave = chave.strip()
            valor = valor.strip().strip('"').strip("'")
            os.environ.setdefault(chave, valor)


def carregar() -> dict:
    _carregar_dotenv(CAMINHO_ENV)
    return {
        "porta": int(os.environ["APP_PORT"]),
        "banco": os.environ["DATABASE_URL"],
    }
