from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token='5935424823:AAEQYLYpI-xEF5JqtTgUvC71VUhzu865w3I')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    await message.reply('Здоров')


@dp.message_handler(commands=['команда'])
async def echo(message: types.Message):
    await message.answer(message.text)


# @dp.message_handler(lambda message: 'такси' in message.text)
# async def taxi(message: types.Message):
#     await message.answer('такси')


@dp.message_handler(lambda message: 'нло' in message.text)
async def ufo(message: types.Message):
    await message.answer('нло')


# @dp.message_handler(lambda message: message.text.startswith('такси'))
@dp.message_handler(lambda message: message.text.startswith('Класс'))
async def ufo(message: types.Message):
    await message.answer(message.text[6:])


@dp.message_handler()
async def empty(message: types.Message):
    await message.answer('Нет такой команды')
    await message.delete()


executor.start_polling(dp, skip_updates=True)
