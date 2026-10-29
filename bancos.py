BANCOS = [
    {
        "id": "caixa",
        "nome": "Caixa",
        "logo": "/static/img/caixa.png",
        "cor": "#0070af",
        "sigla": "CX",
        "produto": "CDB Caixa",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "mercado_pago",
        "nome": "Mercado Pago",
        "logo": "/static/img/mercado-pago.png",
        "cor": "#00a650",
        "sigla": "MP",
        "produto": "Rendimento Mercado Pago",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Confira as condições no aplicativo."
    },
    {
        "id": "nubank",
        "nome": "Nubank",
        "logo": "/static/img/nubank.png",
        "cor": "#820ad1",
        "sigla": "NU",
        "produto": "CDB Nubank",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "inter",
        "nome": "Banco Inter",
        "logo": "/static/img/inter.png",
        "cor": "#ff7a00",
        "sigla": "IN",
        "produto": "CDB Inter",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "btg",
        "nome": "BTG Pactual",
        "logo": "/static/img/btg.png",
        "cor": "#111827",
        "sigla": "BTG",
        "produto": "CDB BTG",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "itau",
        "nome": "Itaú",
        "logo": "/static/img/itau.png",
        "cor": "#ec7000",
        "sigla": "IT",
        "produto": "CDB Itaú",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "bradesco",
        "nome": "Bradesco",
        "logo": "/static/img/bradesco.png",
        "cor": "#cc092f",
        "sigla": "BR",
        "produto": "CDB Bradesco",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "santander",
        "nome": "Santander",
        "logo": "/static/img/santander.png",
        "cor": "#ec0000",
        "sigla": "SAN",
        "produto": "CDB Santander",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "banco_brasil",
        "nome": "Banco do Brasil",
        "logo": "/static/img/banco-brasil.png",
        "cor": "#f7c400",
        "sigla": "BB",
        "produto": "CDB Banco do Brasil",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    },
    {
        "id": "c6",
        "nome": "C6 Bank",
        "logo": "/static/img/c6.png",
        "cor": "#242424",
        "sigla": "C6",
        "produto": "CDB C6",
        "tipo": "cdb_cdi",
        "percentual_cdi": 100,
        "taxa_prefixada": None,
        "taxa_real_ipca": None,
        "observacao": "Taxa ilustrativa. Atualize conforme a oferta oficial."
    }
]


def obter_bancos():
    return BANCOS


def obter_banco_por_id(banco_id):
    for banco in BANCOS:
        if banco["id"] == banco_id:
            return banco
    return None