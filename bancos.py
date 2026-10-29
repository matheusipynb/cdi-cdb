BANCOS = [
    {
        "id": "caixa",
        "nome": "Caixa Econômica Federal",
        "nome_curto": "Caixa",
        "logo": "/static/img/caixa.png",
        "cor": "#0070af",
        "sigla": "CX",
        "site": "https://www.caixa.gov.br",
        "produtos": [
            {
                "id": "caixa_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB que acompanha o CDI. O rendimento varia conforme a taxa durante o período."
            },
            {
                "id": "caixa_poupanca",
                "nome": "Poupança",
                "tipo": "poupanca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Diária",
                "descricao": "Opção simples e de baixo risco, com rendimento geralmente menor que bons CDBs."
            },
            {
                "id": "caixa_tesouro_ipca",
                "nome": "Tesouro IPCA+",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "risco": "Baixo",
                "liquidez": "D+1 após vencimento",
                "descricao": "Título público que protege o poder de compra: rende uma taxa fixa mais a inflação."
            }
        ]
    },
    {
        "id": "mercado_pago",
        "nome": "Mercado Pago",
        "nome_curto": "Mercado Pago",
        "logo": "/static/img/mercado-pago.png",
        "cor": "#00a650",
        "sigla": "MP",
        "site": "https://www.mercadopago.com.br",
        "produtos": [
            {
                "id": "mp_cdb_cdi",
                "nome": "Rendimento do saldo",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Diária",
                "descricao": "Rendimento vinculado a produtos de renda fixa. Confira as regras no aplicativo."
            },
            {
                "id": "mp_cdb_prefixado",
                "nome": "CDB prefixado",
                "tipo": "cdb_prefixado",
                "percentual_cdi": None,
                "taxa_prefixada": 13,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB com taxa fixa combinada na contratação."
            }
        ]
    },
    {
        "id": "nubank",
        "nome": "Nubank",
        "nome_curto": "Nubank",
        "logo": "/static/img/nubank.png",
        "cor": "#820ad1",
        "sigla": "NU",
        "site": "https://www.nubank.com.br",
        "produtos": [
            {
                "id": "nu_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI, indicado para reserva ou objetivos de médio prazo."
            },
            {
                "id": "nu_caixinhas",
                "nome": "Caixinhas",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Varia por caixinha",
                "descricao": "Opções para organizar dinheiro por objetivo, com rendimento geralmente atrelado ao CDI."
            }
        ]
    },
    {
        "id": "inter",
        "nome": "Banco Inter",
        "nome_curto": "Inter",
        "logo": "/static/img/inter.png",
        "cor": "#ff7a00",
        "sigla": "IN",
        "site": "https://www.bancointer.com.br",
        "produtos": [
            {
                "id": "inter_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "inter_lci",
                "nome": "LCI",
                "tipo": "lci_lca",
                "percentual_cdi": 90,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme carência",
                "descricao": "Letra de Crédito Imobiliário, geralmente isenta de Imposto de Renda para pessoa física."
            }
        ]
    },
    {
        "id": "btg",
        "nome": "BTG Pactual",
        "nome_curto": "BTG",
        "logo": "/static/img/btg.png",
        "cor": "#111827",
        "sigla": "BTG",
        "site": "https://www.btgpactual.com",
        "produtos": [
            {
                "id": "btg_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "btg_tesouro_ipca",
                "nome": "Tesouro IPCA+",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "risco": "Baixo",
                "liquidez": "D+1 após vencimento",
                "descricao": "Título público que combina taxa fixa com variação do IPCA."
            }
        ]
    },
    {
        "id": "itau",
        "nome": "Itaú Unibanco",
        "nome_curto": "Itaú",
        "logo": "/static/img/itau.png",
        "cor": "#ec7000",
        "sigla": "IT",
        "site": "https://www.itau.com.br",
        "produtos": [
            {
                "id": "itau_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "itau_fundos",
                "nome": "Fundos de investimento",
                "tipo": "cdb_cdi",
                "percentual_cdi": 95,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo a moderado",
                "liquidez": "Varia por fundo",
                "descricao": "Fundos com diferentes perfis de risco, prazo e rentabilidade."
            }
        ]
    },
    {
        "id": "bradesco",
        "nome": "Bradesco",
        "nome_curto": "Bradesco",
        "logo": "/static/img/bradesco.png",
        "cor": "#cc092f",
        "sigla": "BR",
        "site": "https://www.bradesco.com.br",
        "produtos": [
            {
                "id": "bradesco_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "bradesco_poupanca",
                "nome": "Poupança",
                "tipo": "poupanca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Diária",
                "descricao": "Poupança tradicional, com liquidez diária."
            }
        ]
    },
    {
        "id": "santander",
        "nome": "Santander",
        "nome_curto": "Santander",
        "logo": "/static/img/santander.png",
        "cor": "#ec0000",
        "sigla": "SAN",
        "site": "https://www.santander.com.br",
        "produtos": [
            {
                "id": "santander_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "santander_lca",
                "nome": "LCA",
                "tipo": "lci_lca",
                "percentual_cdi": 90,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme carência",
                "descricao": "Letra de Crédito do Agronegócio, normalmente isenta de IR."
            }
        ]
    },
    {
        "id": "banco_brasil",
        "nome": "Banco do Brasil",
        "nome_curto": "Banco do Brasil",
        "logo": "/static/img/banco-brasil.png",
        "cor": "#f7c400",
        "sigla": "BB",
        "site": "https://www.bb.com.br",
        "produtos": [
            {
                "id": "bb_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "bb_tesouro_ipca",
                "nome": "Tesouro IPCA+",
                "tipo": "tesouro_ipca",
                "percentual_cdi": None,
                "taxa_prefixada": None,
                "taxa_real_ipca": 6.5,
                "risco": "Baixo",
                "liquidez": "D+1 após vencimento",
                "descricao": "Título público que protege contra a inflação."
            }
        ]
    },
    {
        "id": "c6",
        "nome": "C6 Bank",
        "nome_curto": "C6",
        "logo": "/static/img/c6.png",
        "cor": "#242424",
        "sigla": "C6",
        "site": "https://www.c6bank.com.br",
        "produtos": [
            {
                "id": "c6_cdb_cdi",
                "nome": "CDB pós-fixado",
                "tipo": "cdb_cdi",
                "percentual_cdi": 100,
                "taxa_prefixada": None,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB vinculado ao CDI."
            },
            {
                "id": "c6_cdb_prefixado",
                "nome": "CDB prefixado",
                "tipo": "cdb_prefixado",
                "percentual_cdi": None,
                "taxa_prefixada": 13,
                "taxa_real_ipca": None,
                "risco": "Baixo",
                "liquidez": "Conforme vencimento",
                "descricao": "CDB com rentabilidade fixa definida na contratação."
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