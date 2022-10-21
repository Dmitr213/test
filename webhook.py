import os
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher


bot = Bot(token=os.environ["TELEGRAM_TOKEN"])
dp = Dispatcher(bot)


async def webhook_handler(request):
    if request.method == "POST":
        update = request.get_json(force=True)
        text = update['message']['text']
        chat_id = update['message']['chat']['id']
        print(text)

        try:
            await bot.send_message(chat_id=chat_id, text=text)
            return "Webhook processed successfully"
        except Exception as error:
            return "Error in 'webhook_handler': " + str(error)
    else:
        return "request.method in not POST"
