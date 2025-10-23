import os
import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import openai

# 🔑 کلیدها
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_API_KEY

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام 👋 من BestAnalysBot هستم، یه نماد بفرست مثل BTCUSDT تا برات تحلیل کنم 💹")

async def handle_symbol(update: Update, context: ContextTypes.DEFAULT_TYPE):
    symbol = update.message.text.upper().replace("/", "")
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}"
        data = requests.get(url).json()
        price = float(data["lastPrice"])
        high = float(data["highPrice"])
        low = float(data["lowPrice"])

        prompt = f"""
        تحلیل تکنیکال برای {symbol}:
        قیمت فعلی: {price}
        سقف ۲۴ ساعته: {high}
        کف ۲۴ ساعته: {low}
        بر اساس این داده‌ها، حمایت‌ها و مقاومت‌های مهم و نقطه ورود احتمالی رو توضیح بده.
        """

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}]
        )

        reply = response["choices"][0]["message"]["content"]
        await update.message.reply_text(reply)

    except Exception as e:
        await update.message.reply_text("نماد معتبر نیست یا دیتای بایننس در دسترس نیست 😅")

def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_symbol))
    app.run_polling()

if __name__ == "__main__":
    main()
