from aiogram import types, Dispatcher
from create_bot import bot, dp
from keyboards import kb_client
from aiogram.types import ReplyKeyboardRemove
from order import client_order
import sqlite3 as sq


# @dp.message_handler(commands=['start', 'help'])
async def command_start(message: types.Message):
    # global base, cur
    try:
        base = sq.connect('users.db')
        cur = base.cursor()
        cur.execute('INSERT INTO users(user_id,name) VALUES(?,?)',
                    [message.chat.id, message.chat.first_name])
        base.commit()
    except:
        await message.reply('Кнопку "Старт" жмите только один раз')
    try:
        await bot.send_message(message.from_user.id, 'Приятного аппетита',
                               reply_markup=kb_client)
        # reply_markup=kb_client - создаем кастомную клавиатуру
        await message.delete()
    except:
        await message.reply('Общение с ботом через ЛС,напишите '
                            'ему:\nhttps://t.me/Piza_pizaBot')


# @dp.message_handler(commands=['Режим_работы'])
async def pizza_open_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'Вс-Чт с 9:00 до 20:00,'
                                                 'Пт-Сб с 10:00 до 23:00')


# @dp.message_handler(commands=['Расположение'])
async def pizza_place_command(message: types.Message):
    await bot.send_message(message.from_user.id, 'ул.Колбасная 15',
                           reply_markup=ReplyKeyboardRemove())
    # reply_markup=ReplyKeyboardRemove()--удаляем кастомную клавиатуру


# @dp.message_handler(commands=['Меню'])
async def pizza_menu_comand(message: types.Message):
    await client_order.sql_read(message)





def register_handlers_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(pizza_open_command, commands=['Режим_работы'])
    dp.register_message_handler(pizza_place_command, commands=['Расположение'])
    dp.register_message_handler(pizza_menu_comand, commands=['Меню'])