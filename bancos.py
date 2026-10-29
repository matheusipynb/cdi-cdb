BANCOS = [
    {
        "id": "caixa",
        "nome": "Caixa",
        "logo": "/static/img/caixa.png",
        "cor": "#0070af",
        "sigla": "CX",
        "site": "https://www.caixa.gov.br",
        "produtos": [
            {
                "id": "caixa_cdb_cdi",
                "nome": "CDB Caixa pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB que acompanha o CDI. O rendimento depende da variação do CDI até o vencimento."
            },
            {
                "id": "caixa_poupanca",
                "nome": "Poupança Caixa",
                "tipo": "poupanca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Investimento simples e líquido, sem IR sobre o rendimento."
            },
            {
                "id": "caixa_tesouro",
                "nome": "Tesouro Direto via Caixa",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "descricao": "Títulos públicos comprados pela Caixa. Pode ser IPCA+ ou prefixado."
            }
        ]
    },
    {
        "id": "mercado_pago",
        "nome": "Mercado Pago",
        "logo": "/static/img/mercado-pago.png",
        "cor": "#00a650",
        "sigla": "MP",
        "site": "https://www.mercadopago.com.br",
        "produtos": [
            {
                "id": "mp_cdb_cdi",
                "nome": "Rendimento do Mercado Pago",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Saldo remunerado vinculado a produtos de renda fixa. Confira as condições no aplicativo."
            },
            {
                "id": "mp_cdb_prefixado",
                "nome": "CDB Mercado Pago prefixado",
                "tipo": "cdb_prefixado",
                "percentual_cdi": None,
                "taxa_prefixada": 13,
                "taxa_real_ipca": None,
                "descricao": "CDB com taxa fixa definida no momento da aplicação."
            }
        ]
    },
    {
        "id": "nubank",
        "nome": "Nubank",
        "logo": "/static/img/nubank.png",
        "cor": "#820ad1",
        "sigla": "NU",
        "site": "https://www.nubank.com.br",
        "produtos": [
            {
                "id": "nu_cdb_cdi",
                "nome": "CDB Nubank pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB que acompanha o CDI."
            },
            {
                "id": "nu_caixinhas",
                "nome": "Caixinhas do Nubank",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Opções de reserva e objetivos com rendimento vinculado ao CDI."
            }
        ]
    },
    {
        "id": "inter",
        "nome": "Banco Inter",
        "logo": "/static/img/inter.png",
        "cor": "#ff7a00",
        "sigla": "IN",
        "site": "https://www.bancointer.com.br",
        "produtos": [
            {
                "id": "inter_cdb_cdi",
                "nome": "CDB Inter pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "inter_lci",
                "nome": "LCI Inter",
                "tipo": "lci_lca",
                "percentual_cdi": 90,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Letra de Crédito Imobiliário. Geralmente é isenta de IR para pessoa física."
            }
        ]
    },
    {
        "id": "btg",
        "nome": "BTG Pactual",
        "logo": "/static/img/btg.png",
        "cor": "#111827",
        "sigla": "BTG",
        "site": "https://www.btgpactual.com",
        "produtos": [
            {
                "id": "btg_cdb_cdi",
                "nome": "CDB BTG pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "btg_tesouro",
                "nome": "Tesouro Direto via BTG",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "descricao": "Investimento em títulos públicos federais."
            }
        ]
    },
    {
        "id": "itau",
        "nome": "Itaú",
        "logo": "/static/img/itau.png",
        "cor": "#ec7000",
        "sigla": "IT",
        "site": "https://www.itau.com.br",
        "produtos": [
            {
                "id": "itau_cdb_cdi",
                "nome": "CDB Itaú pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "itau_fundos",
                "nome": "Fundos de investimento Itaú",
                "tipo": "cdb_cdi",
                "percentual_cdi": 95,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Fundos com diferentes níveis de risco e rentabilidade."
            }
        ]
    },
    {
        "id": "bradesco",
        "nome": "Bradesco",
        "logo": "/static/img/bradesco.png",
        "cor": "#cc092f",
        "sigla": "BR",
        "site": "https://www.bradesco.com.br",
        "produtos": [
            {
                "id": "bradesco_cdb_cdi",
                "nome": "CDB Bradesco pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "bradesco_poupanca",
                "nome": "Poupança Bradesco",
                "tipo": "poupanca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Poupança tradicional, com liquidez diária."
            }
        ]
    },
    {
        "id": "santander",
        "nome": "Santander",
        "logo": "/static/img/santander.png",
        "cor": "#ec0000",
        "sigla": "SAN",
        "site": "https://www.santander.com.br",
        "produtos": [
            {
                "id": "santander_cdb_cdi",
                "nome": "CDB Santander pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "santander_lca",
                "nome": "LCA Santander",
                "tipo": "lci_lca",
                "percentual_cdi": 90,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "Letra de Crédito do Agronegócio, normalmente isenta de IR."
            }
        ]
    },
    {
        "id": "banco_brasil",
        "nome": "Banco do Brasil",
        "logo": "/static/img/banco-brasil.png",
        "cor": "#f7c400",
        "sigla": "BB",
        "site": "https://www.bb.com.br",
        "produtos": [
            {
                "id": "bb_cdb_cdi",
                "nome": "CDB Banco do Brasil",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "bb_tesouro",
                "nome": "Tesouro Direto via BB",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "descricao": "Investimento em títulos públicos federais."
            }
        ]
    },
    {
        "id": "c6",
        "nome": "C6 Bank",
        "logo": "/static/img/c6.png",
        "cor": "#242424",
        "sigla": "C6",
        "site": "https://www.c6bank.com.br",
        "produtos": [
            {
                "id": "c6_cdb_cdi",
                "nome": "CDB C6 pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "c6_cdb_prefixado",
                "nome": "CDB C6 prefixado",
                "tipo": "cdb_prefixado",
                "percentual_cdi": None,
                "taxa_prefixada": 13,
                "taxa_real_ipca": None,
                "descricao": "CDB com rentabilidade fixa combinada na contratação."
            }
        ]
    }
]


def obter_bancos():
    return BANCOS


def obter_banco_por_id(banco_id):
    for banco in BANCOS:
        if banco["id"] == banco_id:
            return banco
    return None