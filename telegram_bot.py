from help_ import chat_session
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
tokken: Final = 'API_key'           #API_telegram_key
bot_username: Final = '@user_name'  #user_name


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Welcom Back')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Akho dagi s l anglis can i yfehhem wagi')


def handle_response(text: str):
    try:
        return chat_session.send_message(text).text
    except:
        return "Nope, this isn't good or legal"


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    m_t = update.message.chat.type
    text = update.message.text
    print(f'User: {update.message.chat.full_name} in {m_t}: "{text}"')
    response = handle_response(text)
    print('Bot:', response)
    await update.message.reply_text(response)


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == '__main__':
    app = Application.builder().token(tokken).build()
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)
    print('yaa')
    app.run_polling(poll_interval=1)
