import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from database import SaldoDB
from plot_utils import gerar_grafico_em_arquivo
from scheduler import iniciar_agendador
#AGENDADOR DE TAREFAS - REQUISITO PARA PODER CONFIGURAR MENSAGENS AGENDADAS NO BOT
from scheduler import iniciar_agendador
iniciar_agendador()
from telegram import Bot

# Substitua pelo token do seu bot
TELEGRAM_BOT_TOKEN = "SEU_TOKEN_AQUI"

# Log básico
logging.basicConfig(level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou seu assistente de controle de saldo 💰\nUse /saldo, /gasto, /grafico ou /ultimas")

async def saldo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SaldoDB()
    saldo = db.calcular_saldo_atual()
    db.close()
    await update.message.reply_text(f"💰 Saldo atual: R$ {saldo:.2f}")

async def gasto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SaldoDB()
    gasto = db.gasto_diario_permitido()
    db.close()
    await update.message.reply_text(f"📉 Gasto diário permitido: R$ {gasto:.2f}")

async def ultimas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SaldoDB()
    transacoes = db.get_transacoes_ordenadas()[-5:]  # últimas 5
    db.close()
    mensagem = "📋 Últimas transações:\n"
    for data, tipo, valor in transacoes:
        mensagem += f" - {data} | {tipo.upper()} | R$ {valor:.2f}\n"
    await update.message.reply_text(mensagem)

async def grafico(update: Update, context: ContextTypes.DEFAULT_TYPE):
    db = SaldoDB()
    transacoes = db.get_transacoes_ordenadas()
    saldo_inicial = db.get_saldo_inicial()
    db.close()
    caminho = gerar_grafico_em_arquivo(transacoes, saldo_inicial)
    await update.message.reply_photo(photo=open(caminho, 'rb'))

def main():
    app = ApplicationBuilder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("saldo", saldo))
    app.add_handler(CommandHandler("gasto", gasto))
    app.add_handler(CommandHandler("ultimas", ultimas))
    app.add_handler(CommandHandler("grafico", grafico))

    app.run_polling()

if __name__ == "__main__":
    main()

iniciar_agendador()
