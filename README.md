# 💰 Simulador de Investimentos

Aplicação web para simular e comparar investimentos no Brasil, como CDB, poupança, LCI/LCA e Tesouro Direto. O projeto permite escolher uma instituição financeira, selecionar o tipo de investimento, informar valor inicial, aportes mensais e prazo, e visualizar uma estimativa de evolução do patrimônio.

**Acesse o projeto:**  
https://cdi-cdb-3hzk.vercel.app/

## ✨ Funcionalidades

- Simulação de investimentos com valor inicial, aporte mensal e prazo.
- Escolha de banco ou instituição financeira.
- Diferentes tipos de investimento:
  - CDB pós-fixado
  - CDB prefixado
  - LCI / LCA
  - Poupança
  - Tesouro IPCA+
- Cálculo de:
  - Total investido
  - Saldo bruto
  - Rendimento bruto
  - Imposto de Renda
  - Saldo líquido
  - Rendimento líquido
- Comparação automática com a poupança.
- Gráficos interativos de evolução do patrimônio.
- Atualização automática de indicadores econômicos:
  - CDI
  - Selic
  - IPCA
- Interface responsiva para celular, tablet e desktop.
- Explicações simples para usuários iniciantes.

## 🧮 Como funciona a simulação

O simulador utiliza juros compostos e considera aportes mensais.

A fórmula básica é:

[
M = C \times (1 + i)^n
]

Onde:

- (M) é o montante final.
- (C) é o capital inicial.
- (i) é a taxa de juros por período.
- (n) é o número de períodos.

No projeto, a simulação também considera:

- Aportes mensais.
- Imposto de Renda regressivo, quando aplicável.
- Comparação com a poupança.
- Diferença de rentabilidade entre o investimento escolhido e a poupança.

## 🏦 Bancos disponíveis

O projeto possui um catálogo configurável de instituições, incluindo:

- Caixa Econômica Federal
- Mercado Pago
- Nubank
- Banco Inter
- BTG Pactual
- Itaú
- Bradesco
- Santander
- Banco do Brasil
- C6 Bank

Para cada banco, é possível visualizar produtos como CDB, LCI, LCA, poupança, Tesouro Selic, Tesouro IPCA+ e Tesouro Prefixado.

> As taxas dos bancos são configuráveis e servem como base educativa para simulação. Para taxas reais em tempo real por instituição, seria necessária uma integração regulada, como Open Finance.

## 📊 Indicadores automáticos

Os indicadores econômicos são obtidos por meio da API pública do Banco Central do Brasil:

- CDI
- Selic
- IPCA
- TR

Fonte oficial:  
https://dadosabertos.bcb.gov.br/

Os dados são armazenados em cache por 1 hora para evitar chamadas excessivas à API.

## 🛠️ Tecnologias utilizadas

- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Chart.js](https://www.chartjs.org/)
- HTML5
- CSS3
- JavaScript
- [Vercel](https://vercel.com/)

## 📁 Estrutura do projeto

```text
simulador-investimentos/
├── app.py
├── bancos.py
├── calculos.py
├── indicadores.py
├── requirements.txt
├── vercel.json
├── README.md
├── templates/
│   └── index.html
└── static/
    └── style.css