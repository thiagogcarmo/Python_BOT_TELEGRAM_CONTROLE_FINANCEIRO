# 💰 Controle de Saldo com Alerta via Telegram

Um sistema simples e eficiente para **gerenciar seu saldo bancário**, prever o **gasto diário permitido** e receber **alertas no Telegram** quando os limites são ultrapassados.

> Projeto desenvolvido com Python, SQLite, Plotly e integração com Bot do Telegram.

---

## 📌 Funcionalidades

- Inserção de saldo inicial e transações (crédito/débito)
- Cálculo do saldo atual e quanto pode ser gasto por dia
- Geração de gráfico interativo com evolução do saldo
- Bot Telegram com comandos para:
  - Ver saldo atual
  - Ver gasto diário permitido
  - Ver últimas transações
  - Receber gráfico de saldo
- Agendamento diário de resumo automático às 8h
- Alertas instantâneos no Telegram para gastos acima do permitido

---

## 🛠 Tecnologias utilizadas

- Python 3
- SQLite3
- Plotly + Kaleido
- python-telegram-bot
- APScheduler

---

## 🚀 Como usar

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/controle-saldo-bot.git
cd controle-saldo-bot
