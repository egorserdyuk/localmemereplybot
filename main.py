from aiogram import Bot, Dispatcher, executor, types
import os


bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    if message.chat.type in (types.ChatType.GROUP, types.ChatType.SUPERGROUP) and "локальный" in message.text.lower():
        await message.reply_document(document=open("image.webp", "rb"))

executor.start_polling(dp)
