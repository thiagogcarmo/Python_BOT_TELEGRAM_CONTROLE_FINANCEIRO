from apscheduler.schedulers.background import BackgroundScheduler
from telegram import Bot
from datetime import datetime
from database import SaldoDB

TELEGRAM_CHAT_ID = "SEU_CHAT_ID_AQUI"  # Troque pelo seu (veja abaixo)
BOT_TOKEN = "SEU_TOKEN_AQUI"

bot = Bot(token=BOT_TOKEN)

def enviar_resumo_diario():
    db = SaldoDB()
    saldo = db.calcular_saldo_atual()
    gasto = db.gasto_diario_permitido()
    db.close()

    msg = (
        f"📊 *Resumo do dia - {datetime.today().strftime('%d/%m/%Y')}*\n"
        f"💰 Saldo atual: R$ {saldo:.2f}\n"
        f"📉 Gasto diário permitido: R$ {gasto:.2f}"
    )

    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=msg, parse_mode='Markdown')

def iniciar_agendador():
    scheduler = BackgroundScheduler()
    scheduler.add_job(enviar_resumo_diario, 'cron', hour=8, minute=0)
    scheduler.start()
