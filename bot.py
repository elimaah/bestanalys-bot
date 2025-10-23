from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Bot is running successfully!")

async def price(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("💰 Test BTC price: 68520 USD")

def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("price", price))
    app.run_polling()

if __name__ == "__main__":
    main()



