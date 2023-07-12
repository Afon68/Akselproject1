import sqlite3 as sq
from aiogram.dispatcher.filters import Text
from aiogram import types
from aiogram.dispatcher.filters import Command
from create_bot import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,\
    ReplyKeyboardMarkup, KeyboardButton
from data_base import sqlite_db
from data_base import users_db
from datetime import datetime




def sql_start():
    global base, cur
    base = sq.connect(
        'pizza_cool.db')  # connect(), он позволяет подключиться к
    # файлу базы данных, если такого файла не будет он создаёт его, если он
    # есть, то просто подключтся к нему
    cur = base.cursor()  # необходимо создать курсор - это именно та часть
    # базы данных которая осуществляет поиск, встраивание и выборку данных
    # из базы данных.Создаем курсор, он  у нас отталкивается от созданного
    # экземпляра коннекта(base) то есть здесь у нас
    # подключение к базе данных . Курсор запускаем. Здесь просто сделаем
    # такую интересную фишку, когда подключается бот к базе
    # данных, он бы нам выводил в терминал 'Data base connected OK!'.
    if base:  # если к базе данных подклюлчились,то print.......
        print('Data base connected OK!')
    base.execute('CREATE TABLE IF NOT EXISTS menu(img TEXT,name TEXT PRIMARY '
                 'KEY,description TEXT,price TEXT)')

    # base.execute - создаем таблицу, в которую будем вносить данные
    base.commit()  # сохраняем изменения.
    # Так как, мы с вами пишем при помощи модульной системы, для начала нам
    # с вами необходимо запустить этот код( функция sql_start()), то есть
    # необходимо прописать запуск этой функции.У нас есть bot_telegram


async def sql_add_command(state):  # функция,в которую будем
    # записывать изменения в нашу базу данных, state куда и попадает наше
    # состояние словаря
    async with state.proxy() as data:  # открываем этот словарь
        cur = base.cursor()
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)',
                    tuple(data.values()))  # используя наш курсор и команду
        # execute  вставляем в таблицу меню, значения.
        base.commit()  # сохраняем изменения.





# async def sql_add_ord(data):
#     # global base, cur
#     base = sq.connect('orders.db')
#     cur = base.cursor()
#     cur.execute('INSERT INTO orderss(name_pizz) VALUES(?)', (data,))
#     base.commit()

async def sql_read2():
    return cur.execute('SELECT * FROM menu').fetchall()


async def sql_delete_command(data):
    cur.execute('DELETE FROM menu WHERE name == ?', (data,))
    base.commit()

# def register_handlers_sqlite_db(dp: Dispatcher):
#     dp.register_message_handler(sql_insert_us, commands=['start', 'help'])
