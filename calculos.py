from math import pow


def taxa_mensal(taxa_aa):
    """Converte uma taxa anual percentual em taxa mensal composta."""
    return pow(1 + taxa_aa / 100, 1 / 12) - 1


def calcular_ir(meses, ir_personalizado=None):
    """
    Tabela regressiva simplificada de IR para CDB/RDB:
    - Até 180 dias: 22,5%
    - 181 a 360 dias: 20%
    - 361 a 720 dias: 17,5%
    - Acima de 720 dias: 15%
    """
    if ir_personalizado and ir_personalizado > 0:
        return ir_personalizado

    if meses <= 6:
        return 22.5
    elif meses <= 12:
        return 20
    elif meses <= 24:
        return 17.5
    return 15


def rendimento_poupanca_mensal(selic_aa, tr_mensal):
    """
    Regra da poupança:
    - Selic acima de 8,5% a.a.: 0,5% ao mês + TR
    - Selic até 8,5% a.a.: 70% da Selic + TR
    """
    if selic_aa > 8.5:
        return 0.5 + tr_mensal

    return (selic_aa * 0.70) / 12 + tr_mensal


def evoluir_saldo(valor_inicial, aporte, taxa_m, meses, ir_percentual=None):
    """
    Calcula mês a mês:
    - saldo com juros compostos
    - aportes mensais
    - IR opcional no resgate
    """
    saldo = valor_inicial
    total_aportado = valor_inicial
    historico = []

    for mes in range(1, meses + 1):
        saldo += aporte
        total_aportado += aporte
        saldo *= 1 + taxa_m

        historico.append({
            "mes": mes,
            "aportado": round(total_aportado, 2),
            "saldo_bruto": round(saldo, 2),
            "rendimento_bruto": round(saldo - total_aportado, 2)
        })

    rendimento_bruto = saldo - total_aportado

    if ir_percentual is None or ir_percentual <= 0:
        ir_valor = 0
        saldo_liquido = saldo
        rendimento_liquido = rendimento_bruto
    else:
        ir_valor = rendimento_bruto * (ir_percentual / 100)
        saldo_liquido = saldo - ir_valor
        rendimento_liquido = rendimento_bruto - ir_valor

    return {
        "total_aportado": round(total_aportado, 2),
        "saldo_bruto": round(saldo, 2),
        "rendimento_bruto": round(rendimento_bruto, 2),
        "ir_valor": round(ir_valor, 2),
        "saldo_liquido": round(saldo_liquido, 2),
        "rendimento_liquido": round(rendimento_liquido, 2),
        "historico": historico
    }


def simular(
    tipo,
    valor_inicial,
    aporte_mensal,
    meses,
    cdi_aa,
    percentual_cdi,
    taxa_prefixada_aa,
    ipca_aa,
    tr_mensal,
    ir_percentual
):
    if valor_inicial < 0 or aporte_mensal < 0:
        raise ValueError("Valores não podem ser negativos.")

    if meses <= 0:
        raise ValueError("O prazo deve ser maior que zero.")

    cdi_mensal = taxa_mensal(cdi_aa)
    selic_aproximada = cdi_aa + 0.10

    if tipo == "cdb_cdi":
        taxa_m = cdi_mensal * (percentual_cdi / 100)
        ir = calcular_ir(meses, ir_percentual)
        resultado = evoluir_saldo(valor_inicial, aporte_mensal, taxa_m, meses, ir)
        nome = f"CDB {percentual_cdi}% do CDI"

    elif tipo == "cdb_prefixado":
        if taxa_prefixada_aa <= 0:
            raise ValueError("Informe a taxa prefixada anual do CDB.")

        taxa_m = taxa_mensal(taxa_prefixada_aa)
        ir = calcular_ir(meses, ir_percentual)
        resultado = evoluir_saldo(valor_inicial, aporte_mensal, taxa_m, meses, ir)
        nome = f"CDB prefixado {taxa_prefixada_aa}% a.a."

    elif tipo == "lci_lca":
        taxa_m = cdi_mensal * (percentual_cdi / 100)
        resultado = evoluir_saldo(valor_inicial, aporte_mensal, taxa_m, meses, 0)
        nome = f"LCI/LCA {percentual_cdi}% do CDI"

    elif tipo == "poupanca":
        taxa_m = rendimento_poupanca_mensal(selic_aproximada, tr_mensal) / 100
        resultado = evoluir_saldo(valor_inicial, aporte_mensal, taxa_m, meses, 0)
        nome = "Poupança"

    elif tipo == "tesouro_ipca":
        if taxa_prefixada_aa <= 0:
            raise ValueError("Informe a taxa real anual do Tesouro IPCA+.")

        taxa_real_mensal = taxa_mensal(taxa_prefixada_aa)
        inflacao_mensal = taxa_mensal(ipca_aa)
        taxa_m = (1 + taxa_real_mensal) * (1 + inflacao_mensal) - 1

        ir = calcular_ir(meses, ir_percentual)
        resultado = evoluir_saldo(valor_inicial, aporte_mensal, taxa_m, meses, ir)
        nome = f"Tesouro IPCA+ {taxa_prefixada_aa}% a.a."

    else:
        raise ValueError("Tipo de investimento inválido.")

    poupanca_m = rendimento_poupanca_mensal(selic_aproximada, tr_mensal) / 100
    comparacao = evoluir_saldo(valor_inicial, aporte_mensal, poupanca_m, meses, 0)

    diferenca = resultado["saldo_liquido"] - comparacao["saldo_liquido"]

    return {
        "investimento": nome,
        "tipo": tipo,
        "meses": meses,
        "taxa_mensal_aproximada": round(taxa_m * 100, 4),
        **resultado,
        "comparacao_poupanca": {
            "saldo_liquido": comparacao["saldo_liquido"],
            "rendimento_liquido": comparacao["rendimento_liquido"],
            "diferenca_a_favor": round(diferenca, 2),
            "historico": comparacao["historico"]
        }
    }