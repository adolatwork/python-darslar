from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from translate import Translator

def translate_to_english(text):
    translator = Translator(from_lang="uz", to_lang="en")
    return translator.translate(text)

def start(update, context):
    update.message.reply_text(
        "Assalomu alaykum! 🇺🇿➡️🇬🇧\n"
        "Menga o'zbekcha so'z yuboring, men uni ingliz tiliga tarjima qilib beraman."
    )

def translate_message(update, context):
    uzbek_text = update.message.text
    try:
        english_translation = translate_to_english(uzbek_text)
        update.message.reply_text(f"🇬🇧 Tarjima: {english_translation}")
    except Exception:
        update.message.reply_text("Tarjima vaqtida xatolik yuz berdi.")

def main():
    TOKEN = "6853590365:AAF6Htln05CgNvUcrQed0Q9jdnsAnb147eU"  # <-- SHU YERGA BOT TOKENINGIZNI YAZING

    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, translate_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
