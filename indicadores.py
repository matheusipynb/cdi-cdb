from datetime import datetime

import requests
from flask import current_app

BCB_BASE = "https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados"

SERIES = {
    "selic_meta": 432,
    "ipca": 433,
    "tr": 226,
    "cdi": 4389
}

CACHE_SEGUNDOS = 3600


def buscar_serie(codigo, ultimos=13):
    url = f"{BCB_BASE.format(codigo=codigo)}/ultimos/{ultimos}?formato=json"

    resposta = requests.get(url, timeout=10)
    resposta.raise_for_status()

    dados = resposta.json()

    return [
        {
            "data": item["data"],
            "valor": float(str(item["valor"]).replace(",", "."))
        }
        for item in dados
    ]


def obter_indicadores():
    agora = datetime.utcnow()
    cache = current_app.extensions.get("cache_indicadores")

    if cache:
        segundos = (agora - cache["atualizado_em"]).total_seconds()

        if segundos < CACHE_SEGUNDOS:
            return cache["dados"]

    indicadores = {}

    for nome, codigo in SERIES.items():
        try:
            historico = buscar_serie(codigo, ultimos=13)

            indicadores[nome] = {
                "atual": historico[-1]["valor"],
                "data": historico[-1]["data"],
                "historico": historico
            }

        except Exception:
            indicadores[nome] = {
                "atual": None,
                "data": None,
                "historico": [],
                "erro": "Não foi possível obter os dados agora."
            }

    dados = {
        "atualizado_em": agora.isoformat(),
        "fonte": "Banco Central do Brasil — SGS/BCData",
        "indicadores": indicadores
    }

    current_app.extensions["cache_indicadores"] = {
        "atualizado_em": agora,
        "dados": dados
    }

    return dados