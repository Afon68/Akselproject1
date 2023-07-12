import sqlite3 as sq
from aiogram.dispatcher.filters import Text
from aiogram import types
from create_bot import bot, dp
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton,\
    ReplyKeyboardMarkup, KeyboardButton
from data_base import sqlite_db
from data_base import users_db
from datetime import datetime
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove


async def sql_read(message):
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    for ret in cur.execute('SELECT * FROM menu').fetchall():  #
        # fetchall()
        # применяем этот метод, который выгружает все сюда в виде списка,
        # все данные из таблицы получается список из строк
        await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n'
                        f'Описание:{ret[2]}\nЦена:{ret[-1]}',
            reply_markup=InlineKeyboardMarkup().add(
                InlineKeyboardButton
             (f'Заказать {ret[1]}', callback_data=f'ord {ret[1]}')))


@dp.callback_query_handler(Text(startswith='ord '))
async def del_callback_ord(callback_query: types.CallbackQuery,):
    inkb = InlineKeyboardMarkup(row_width=2).add(InlineKeyboardButton(
        f"{callback_query.data.replace('ord ', '')} С доставкой",
                                           callback_data='С дост'), InlineKeyboardButton(
        'Без доставки', callback_data='Без дост'))
    await bot.send_message(callback_query.message.chat.id,
                           f"{callback_query.data.replace('ord ', '')}: Вы "
                            'хотите?', reply_markup=inkb)
    # data = state.proxy()
    # base = sq.connect('orders.db')
    # cur = base.cursor()
    # # datetime.now()-текущее время;strftime("%d.%m.%Y %I:%M:%S")-нужный формат
    # cur.execute('INSERT INTO orderss(date_time_ord,user_id,name_us,'
    #             'name_pizz) VALUES(?,?,?,?)',
    #             [datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
    #              callback_query.message.chat.id,
    #              callback_query.message.chat.first_name,
    #              callback_query.data.replace('ord ', ''),await sql_add_ord(state)])
    # async with state.proxy() as data:
    #     cur.execute('INSERT INTO orderss(address) VALUES(?)',
    #                 tuple(data.values()))

    # base.commit()
        # await callback_query.answer(text=f"{callback_query.data.replace('ord ', '')}."
        #                                  f' Ваш заказ уже выполняется.',
        #                             show_alert=True)


class FSMord(StatesGroup):
    address = State()
    date = State()
    time = State()


# answ = dict()
@dp.callback_query_handler(Text(endswith='дост'))
# @dp.message_handler(state=None)
async def delivery(callback: types.CallbackQuery):
    res = callback.data.split()[0]
    if res == 'С':
        await FSMord.address.set()
        await callback.answer('В поле сообщений укажите пожалуйста адрес '
                              'доставки ',
                              show_alert=True)
    else:
        await callback.answer('Приходите к нам!!!Мы с удовольствием Вас '
                              'обслужим по адресу "ул.Колбасная 15".Мы ждем '
                              'Вас ❤️', show_alert=True)
                              # show_alert=True)
        await callback.message.answer('Приходите к нам!!!Мы с удовольствием '
                                      'Вас ' 'обслужим по адресу '
                                      '"ул.Колбасная 15".Мы ждем '
                                                  'Вас ❤️')


@dp.message_handler(state=FSMord.address)
async def load_adress(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
       data['address'] = message.text
    # await state.update_data(adress=message.text)
    # adr = await state.get_data()
    # await message.answer(f"Адрес: {data['address']}")
    await FSMord.next()
    await message.reply('Теперь укажи дату доставки')

    # async with state.proxy() as data:
    # await message.reply(str(data))
    # await sqlite_db.sql_add_command(state) # нам сюда необходимо
    # передать вот этот полученный словарь. Этот словарь у нас находится
    # под именем state, там комплексный объект машины состояний(async
    # with state( Этот state).proxy() as data:)
    # await state.finish()
    # await sql_add_ord(state)


@dp.message_handler(state=FSMord.date)
async def load_date(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['date'] = message.text
    # await message.answer(f"Адрес: {data['date']}")
    await FSMord.next()
    await message.reply('Теперь укажи время доставки')



@dp.message_handler(state=FSMord.time)
async def load_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.text
        await FSMord.next()
       # await message.reply('И так продолжим')
    base = sq.connect('pizza_cool.db')
    cur = base.cursor()
    for ret in cur.execute('SELECT * FROM menu').fetchall():

        # fetchall()
        # применяем этот метод, который выгружает все сюда в виде списка,
        # все данные из таблицы получается список из строк
        # await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n',
        #                                f'Описание:{ret[2]}\nЦена:{ret[-1]}')
        inkb_ord = InlineKeyboardMarkup().add(InlineKeyboardButton
                 ('Подтвердить', callback_data=f'qwe {ret[1]}'))
        await bot.send_message(message.from_user.id,
            f"Подтвердите заказ '{ret[1]}'", reply_markup=inkb_ord)

            # async with state.proxy() as data:
        #     await message.reply(str(data))
        # await sql_add_ord(state)  # нам сюда необходимо
        # передать вот этот полученный словарь. Этот словарь у нас находится
        # под именем state, там комплексный объект машины состояний(async
        # with state( Этот state).proxy() as data:)


@dp.callback_query_handler(Text(startswith='qwe '))
async def sql_all_ord(callback_query: types.CallbackQuery, state: FSMContext):
    await callback_query.answer('Супер ❤️')
    # data = state.proxy()
    base = sq.connect('orders.db')
    cur = base.cursor()
    # datetime.now()-текущее время;strftime("%d.%m.%Y %I:%M:%S")-нужный формат
    cur.execute('INSERT INTO orderss (date_time_ord,user_id,name_us,'
                'name_pizz,address) '
                'VALUES(?,?,?,?,?)',
                (datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
                 callback_query.message.chat.id,
                 callback_query.message.chat.first_name,
                 callback_query.data.replace('qwe ', ''),
                 await sql_add_ord(state)))
    await callback_query.message.answer('Cпосибо за введенную информацию!!!❤️')
                                # show_alert=True)
    base.commit()

    await callback_query.message.answer('❤️')
    await callback_query.message.answer('Ожидайте пожалуйста заказ!!!❤️')
    await state.finish()



async def sql_add_ord(state):
    async with state.proxy() as data:  # открываем этот словарь
        base = sq.connect('orders.db')
        cur = base.cursor()
        cur.execute('INSERT INTO orderss(address,date_execute,time_execute)'
                    ' VALUES(?,?,?)',
                    tuple(data.values()))  # используя наш курсор и команду
        # execute  вставляем в таблицу меню, значения.
        base.commit()  # сохраняем изменения.




# message: types.Message, state: FSMContext
# async def add_orders():
# SMContextProxy state = 'FSMord:adress',
# data = {'adress': 'fghfgxhfxh'}, closed = True

