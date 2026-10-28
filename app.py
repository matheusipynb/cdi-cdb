from flask import Flask, render_template, request, jsonify
from calculos import simular
from indicadores import obter_indicadores

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


@app.route("/api/simular", methods=["POST"])
def api_simular():
    dados = request.get_json(silent=True) or {}

    try:
        cdi_aa = float(dados.get("cdi_aa", 13.65))

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
            percentual_cdi=float(dados.get("percentual_cdi", 100)),
            taxa_prefixada_aa=float(dados.get("taxa_prefixada_aa", 0)),
            ipca_aa=float(dados.get("ipca_aa", 4.5)),
            tr_mensal=float(dados.get("tr_mensal", 0.17)),
            ir_percentual=float(dados.get("ir_percentual", 0)),
        )

        return jsonify({"ok": True, "resultado": resultado})

    except Exception as erro:
        return jsonify({"ok": False, "erro": str(erro)}), 400


# Necessário para a Vercel encontrar o app Flask
app_instance = app