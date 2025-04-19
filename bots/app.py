import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.filters import Command, CommandStart
from aiogram.types import Message


from googletrans import Translator

# Bot token can be obtained via https://t.me/BotFather
TOKEN = "6853590365:AAF6Htln05CgNvUcrQed0Q9jdnsAnb147eU"

# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()
translator = Translator()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@dp.message(Command("translate"))
async def translate_handler(message: Message) -> None:
    """
    Translate command handler.
    Usage: /translate <lang_code> <text>
    Example: /translate es Hello, how are you?
    """
    args = message.text.split(maxsplit=2)

    if len(args) < 3:
        await message.answer("Usage: /translate <lang_code> <text>\nExample: /translate es Hello")
        return

    target_lang = args[1]
    text_to_translate = args[2]

    try:
        result = translator.translate(text_to_translate, dest=target_lang)
        await message.answer(f"🔤 Translated ({target_lang}): {result.text}")
    except Exception as e:
        await message.answer(f"❌ Translation failed: {e}")


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    try:
        # Send a copy of the received message
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        # But not all the types is supported to be copied so need to handle it
        await message.answer("Nice try!")


async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.delete_webhook(drop_pending_updates=True)

    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
