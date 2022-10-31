import wikipedia


from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = "5562021563:AAESXycLLpInVbRaLmh9RfFOKm87fucrngQ"
wikipedia.set_lang('UZ')

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help']) 
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Assalomu Alykum")



@dp.message_handler()
async def echo(message: types.Message):
    try:
        wikipedia.set_lang('uz')
        response=wikipedia.summary(message.text)
        await message.answer(response)
    except:
        await message.answer('this news couldnt be found')


  
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)