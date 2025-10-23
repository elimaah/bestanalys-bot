from telegram.ext import ApplicationBuilder, CommandHandler
import os

TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")

async def start(update, context):
    await update.message.reply_text("سلام دلنشین جان 🌸 ربات فعاله!")

app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()


if __name__ == "__main__":
    main()


