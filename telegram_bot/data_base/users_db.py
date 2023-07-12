import sqlite3 as sq
# from aiogram.dispatcher.filters import Command


def sql_create_user():
    global base, cur
    base = sq.connect('users.db')
    cur = base.cursor()
    # base.execute('DROP TABLE IF  EXISTS users')
    base.execute('CREATE TABLE IF NOT EXISTS users(ID INTEGER PRIMARY KEY '
                 'AUTOINCREMENT,'
                 ' user_id int, name TEXT,'
                 ' CONSTRAINT user_id_unique UNIQUE (user_id))')
    base.commit()


# @dp.message_handler(Command('start'))
# async def sql_insert_us(message: types.Message):
#     cur.execute('INSERT INTO users(user_id,name) VALUES(?,?)',
#                 (message.chat.id, message.chat.first_name))
#     base.commit()

def sql_create_order():
    global base, cur
    base = sq.connect('orders.db')
    cur = base.cursor()
    # base.execute('DROP TABLE IF  EXISTS orderss')
    base.execute('CREATE TABLE IF NOT EXISTS orderss(ID INTEGER PRIMARY KEY '
                 'AUTOINCREMENT,date_time_ord TEXT,user_id int,'
                 'name_us TEXT, name_pizz TEXT , address TEXT,'
                 'date_execute TEXT,time_execute TEXT, status TEXT)')

    base.commit()

# async def write_order():
#     cur.execute('INSERT INTO users(user_id,name_us) VALUES(?,?)',
#                 (message.chat.id, message.chat.first_name))
#     base.commit()

async def sql_add_adress(state):  # функция,в которую будем
    # записывать изменения в нашу базу данных, state куда и попадает наше
    # состояние словаря
    async with state.proxy() as data:  # открываем этот словарь
        cur = base.cursor()
        cur.execute('INSERT INTO menu VALUES(?, ?, ?, ?)',
                    tuple(data.values()))  # используя наш курсор и команду
        # execute  вставляем в таблицу меню, значения.
        base.commit()  # сохраняем изменения.