from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from create_bot import bot, dp
from aiogram.dispatcher.filters import Text
from data_base import sqlite_db
from keyboards import admin_kb
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ID = None  # Константа

'''теперь для начала нам необходимо создать класс наших состояний '''


# Рассмотрим последовательность State, наследование от класса StatesGroup
class FSMAdmin(StatesGroup):
    photo = State()  # Запуск класса State() -- состоянии бота
    name = State()
    description = State()
    price = State()
# класс State необходим для того, чтобы бот переходил между этими
# состояниями,которые мы пропишем этот переход в хендлерах

'''Получаем ID текущего модератора'''


# @dp.message_handler(commands=['moderator'],is_chat_admin=True)
async def make_changes_command(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot.send_message(message.from_user.id, 'Что хозяин надо???',
                                reply_markup = admin_kb.button_case_admin)
    await message.delete()
# commands=['moderator'],is_chat_admin=True -- если админ чато нашей группы
# пишет команду--'/moderator'. Как только пользователь вводит команду
# модератор и он у нас все-таки является модератором группы, мы с вами
# объявляем здесь эту переменную ID глобальной и присваиваем в нее id-дишник
# этого пользователя и администратора соответственно  message.from_user.id
# получаем его id-иш ник, присваиваем в  переменную ID, далее пишем, причем
# обратите внимание, что администратор должен написать именно не боту,
# а в группу, для того чтобы бот взял  id-ишник пользователя и проверил его на
# права доступа, далее бот просто пишет ему уже в личку 'Что хозяин надо'

'''Начало диалога загрузки нового пункта меню'''


# @dp.message_handler(commands='Загрузить',state = None)
async def cm_start(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото')
# state = None Указываем  дополнительный параметр, то есть состояние здесь
# записываем нам так как это у нас хендлер старта,а он еще бот не находится
# в состоянии  машины состояний.
#   Как только админ пишет '/Загрузить' срабатывает
# этот хендлер, мы здесь становимся ботом в состоянии загрузки, то есть он
# теперь будет ожидать конкретного ответа от пользователя, то есть
# перейдет из обычного режима работы в режим работы машины состояний. Именно
# благодаря тому, что мы здесь устанавливаем FSMAdmin.photo.set()
#  бот переходит в этот режим.

'''Выход из состояний'''

# @dp.message_handler(state='*', commands='отмена')
# @dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state() # текущее машинное состояние пользователя
        if current_state is None:
            return
        await state.finish()
        await message.reply('OK')
# state='*- в каком бы в данном случае из 4 состояний бот не находился
# Text(equals='отмена', ignore_case=True), state='*'--здесь у нас фильтр текста
# то есть здесь записываем какой конкретно текст -'отмена'и как бы ни
# написал (ignore_case=True) и состоянии то же самое любое (state='*')

'''Ловим первый ответ и пишем в словарь'''


# @dp.message_handler(content_types=['photo'], state=FSMAdmin.photo)
async def load_photo(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['photo'] = message.photo[0].file_id
        await FSMAdmin.next() # переводим  нашего бота в ожидание следующего
                                                               # ответа
        await message.reply('Теперь введи название')
# state=FSMAdmin.photo так как мы поставили нашего бота здесь в  состоянии
# ожидания ответа на первый вопрос. Именно благодаря
# этому, так как мы сюда передаем  этот аргумент state=FSMAdmin.photo, bot
# понимает, что именно в этот хендлер попадет первый ответ от пользователя!

'''Ловим второй ответ'''


# @dp.message_handler(state=FSMAdmin.name)
async def load_name(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание')


'''Ловим третий ответ'''


# @dp.message_handler(state=FSMAdmin.description)
async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Теперь укажи цену')


'''Ловим последний ответ и используем полученные данные'''


# @dp.message_handler(state=FSMAdmin.price)
async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = float(message.text)
                    # async with state.proxy() as data:
        #     await message.reply(str(data))
        await sqlite_db.sql_add_command(state) # нам сюда необходимо
        # передать вот этот полученный словарь. Этот словарь у нас находится
        # под именем state, там комплексный объект машины состояний(async
        # with state( Этот state).proxy() as data:)
        await state.finish()


# @dp.callback_query_handler(lambda x: x.data and x.data.startswith('del '))
@dp.callback_query_handler(Text(startswith='del '))
async def del_callback_run(callback_query: types.CallbackQuery):
    await sqlite_db.sql_delete_command(callback_query.data.replace('del ', ''))
    await callback_query.answer(text=f"{callback_query.data.replace('del ', '')}"
                                     f' удалена.', show_alert=True)
# callback_query - этот параметр можно называть как угодно

@dp.message_handler(commands='Удалить')
async def delete_item(message: types.Message):
    if message.from_user.id == ID:
        read = await sqlite_db.sql_read2()
        for ret in read:
            await bot.send_photo(message.from_user.id, ret[0], f'{ret[1]}\n'
                                f'Описание:{ret[2]}\nЦена:{ret[-1]}')
            await bot.send_message(message.from_user.id, text= '???',
            reply_markup=InlineKeyboardMarkup().add(InlineKeyboardButton(
            f'Удалить {ret[1]}', callback_data=f'del {ret[1]}')))


'''Регистрируем хендлеры'''


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(make_changes_command, commands=['moderator'],is_chat_admin=True)
    dp.register_message_handler(cm_start, commands=['Загрузить'], state=None)
    dp.register_message_handler(cancel_handler, state='*', commands='отмена')
    dp.register_message_handler(cancel_handler, Text(equals='отмена',
                                                     ignore_case=True),
                                state='*')
    dp.register_message_handler(load_photo, content_types=['photo'],
                                state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.callback_query_handler(del_callback_run, lambda x: x.data and
                                                x.data.startswith('del '))
    dp.register_message_handler(delete_item, commands='Удалить')






'''ПОЛУЧЕННЫЕ ДАННЫЕ

--FSMContextProxy state = 'FSMAdmin:price', data = {
'photo': 
'AgACAgIAAxkBAAIBEmP09k3UUcP9uBXOY8aDqQdVm9JDAALqxDEbWsGoS1g0aKP5AAH
-9wEAAwIAA3MAAy4E', 'name': 'Волщебные летающие овощи', 'description': 
'Очень быстро готовятся', 'price': 36.0} '''
