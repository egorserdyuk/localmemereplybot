from aiogram import Bot, Dispatcher, executor, types
import os


bot = Bot(token=os.environ["TELEGRAM_TOKEN"])

dp = Dispatcher(bot)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def handle_text(message: types.Message):
    """
    Asynchronous function that handles text messages by replying with an image document, 
    if the message is received in a group or supergroup chat and contains the substring "локальный" (localized in Russian).

    Args:
    - message: A message object of type types.Message, which represents the message to be processed.

    Returns:
    - None
    """
    if message.chat.type in (types.ChatType.GROUP, types.ChatType.SUPERGROUP) and "локальный" in message.text.lower():
        await message.reply_document(document=open("image.webp", "rb"))


if __name__ == "__main__":
    executor.start_polling(dp)
