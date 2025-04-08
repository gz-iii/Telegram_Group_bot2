import logging
import re
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

BOT_TOKEN = "7433782931:AAFEdGEabnqlN1omdatoZJx_CNNYcejeFSA"

def contains_link(text: str) -> bool:
    return bool(re.search(r'(https?://|t\.me/|www\.)', text))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message

    if not message:
        return

    if message.text and contains_link(message.text):
        try:
            await message.delete()
            logging.info("删除了包含链接的消息。")
        except Exception as e:
            logging.warning(f"无法删除消息：{e}")
        return

    if message.forward_from_chat or message.forward_from:
        try:
            await message.delete()
            logging.info("删除了引用外部消息的消息。")
        except Exception as e:
            logging.warning(f"无法删除消息：{e}")

async def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.ALL, handle_message))
    await app.run_polling()

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())
