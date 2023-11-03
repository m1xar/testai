from telegram.ext import Application, MessageHandler, filters

from logic import query_engine

TOKEN = '6944848846:AAFkQFzpC__Y_nZZhq5ZnzvfEanj8lhL1Kw'


async def handle_message(update, context):
    text = update.message.text
    print(f'User: {text}')

    response = query_engine.query(text)
    print(f'Bot: {response}')

    await update.message.reply_text(response.response)


async def error(update, context):
    print(context.error)


if __name__ == '__main__':
    print('Starting...')
    app = Application.builder().token(TOKEN).build()

    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    app.add_error_handler(error)

    app.run_polling(poll_interval=1)