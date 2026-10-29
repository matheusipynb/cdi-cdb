from flask import Flask, render_template, request, jsonify
from calculos import simular
from indicadores import obter_indicadores
from bancos import obter_bancos, obter_banco_por_id

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/indicadores")
def api_indicadores():
    try:
        dados = obter_indicadores()
        return jsonify({"ok": True, "dados": dados})
    except Exception as erro:
        return jsonify({"ok": False, "erro": str(erro)}), 500


@app.route("/api/bancos")
def api_bancos():
    return jsonify({
        "ok": True,
        "bancos": obter_bancos()
    })


@app.route("/api/simular", methods=["POST"])
def api_simular():
    dados = request.get_json(silent=True) or {}

    try:
        cdi_aa = float(dados.get("cdi_aa", 13.65))
        percentual_cdi = float(dados.get("percentual_cdi", 100))
        taxa_prefixada_aa = float(dados.get("taxa_prefixada_aa", 0))
        taxa_real_ipca = float(dados.get("taxa_real_ipca", 0))

        banco_id = dados.get("banco_id")

        if banco_id:
            banco = obter_banco_por_id(banco_id)

            if banco:
                percentual_cdi = banco.get("percentual_cdi") or percentual_cdi
                taxa_prefixada_aa = banco.get("taxa_prefixada") or taxa_prefixada_aa
                taxa_real_ipca = banco.get("taxa_real_ipca") or taxa_real_ipca

        if dados.get("usar_cdi_automatico"):
            indicadores = obter_indicadores()
            cdi_atual = indicadores["indicadores"]["cdi"]["atual"]

            if cdi_atual:
                cdi_aa = cdi_atual

        resultado = simular(
            tipo=dados.get("tipo", "cdb_cdi"),
            valor_inicial=float(dados.get("valor_inicial", 0)),
            aporte_mensal=float(dados.get("aporte_mensal", 0)),
            meses=int(dados.get("meses", 12)),
            cdi_aa=cdi_aa,
            percentual_cdi=percentual_cdi,
            taxa_prefixada_aa=taxa_prefixada_aa,
            ipca_aa=float(dados.get("ipca_aa", 4.5)),
            tr_mensal=float(dados.get("tr_mensal", 0.17)),
            ir_percentual=float(dados.get("ir_percentual", 0)),
        )

        return jsonify({
            "ok": True,
            "resultado": resultado
        })

    except Exception as erro:
        return jsonify({"ok": False, "erro": str(erro)}), 400


app_instance = app