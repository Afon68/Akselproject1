from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor
from aiogram.dispatcher.filters import Text

# bot = Bot(token=os.getenv('TOKEN'))# инициализируем нашего бота
bot = Bot(token='5935424823:AAEQYLYpI-xEF5JqtTgUvC71VUhzu865w3I')  # запуск
# класса Bot,в параметре token из telegram - BotFather?(надеюсь ,что так)
dp = Dispatcher(bot)

answ = dict()

'''                  Кнопка ссылка            '''
urlkb = InlineKeyboardMarkup(
    row_width=1)  # создаем клавиатуру(row_width=1 - кол-во кнопок в ряду)
urlbutton = InlineKeyboardButton(text='ссылка', url='https://youtube.com')
urlbutton2 = InlineKeyboardButton(text='ссылка2', url='https://google.com')
x = [InlineKeyboardButton(text='ссылка3', url='https://google.com'),
     InlineKeyboardButton('ссылка4', url='https://google.com'),
     InlineKeyboardButton(text='ссылка5', url='https://google.com'),
     InlineKeyboardButton(text='ссылка6', url='https://google.com')]
urlkb.add(urlbutton, urlbutton2).row(*x).insert(InlineKeyboardButton
                                    ('ссылка7', url='https://google.com'))
# text='ссылка6' -  cлово 'text' писать необязательно,работает по любому

# row_width=1 - кол-во кнопок в ряду( ширина ряда),думаю для add

@dp.message_handler(commands='ссылки')
async def url_comand(message: types.Message):
    await message.answer('ссылочки:', reply_markup=urlkb)


# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(
#     text='Нажми меня', callback_data='www')

inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(
    text='Like', callback_data='like_1'), InlineKeyboardButton(
    'No Like', callback_data='like_-1'))

'''Ниже заменил like_1 на like_yes и like_-1 на like_no и в def www_call 
заменил int(callback.data.split('_')[1])  на callback.data.split('_')[1] - 
после этих изменений все работало нормально '''

# inkb = InlineKeyboardMarkup(row_width=1).add(InlineKeyboardButton(
#     text='Like', callback_data='like_yes'), InlineKeyboardButton(
#     text='No Like', callback_data='like_no'))
# второй аргумент нам необходимо с вами передать в параметр  callback_data, то
# что имя события, которое произойдет, то есть по сути мы сюда с вами передаём
# обычную строку, ну например вплоть до того, что здесь написать 'www' -  это
# уже
# будет событие. Нажимая на эту кнопку, в чем суть, вот этот строка
# отправляется незримо для пользователя нашему боту, которую мы с вами и
# улавливаем специальным хейндлером

# @dp.message_handler(commands='test')
# async def test_commands(message: types.Message):
#     await message.answer('Инлайн кнопка', reply_markup=inkb)

@dp.message_handler(commands='test')
async def test_commands(message: types.Message):
    await message.answer('За видео про деплой бота', reply_markup=inkb)


# @dp.callback_query_handler(text='www')
# async def www_call(callback: types.CallbackQuery):
#     await callback.message.answer('Нажата инлайн кнопка')
#     await callback.answer('Нажата инлайн пробка',show_alert=True)
'''Лектор (Python Hub Studio) использует f-строку в 
answ[f'{callback.from_user.id}] и соответственно её надо применить в 
if callback.from_user.id not in answ,лектор этого не сделал,упустил из виду  
и интепритатор его поправил. Но я попробывал сделать без f-строки и да 
!!!....у меня всё получилось - код рабатает!
'''
@dp.callback_query_handler(Text(startswith='like_'))
async def www_call(callback: types.CallbackQuery):
    res = int(callback.data.split('_')[1])
    if callback.from_user.id not in answ:
        answ[callback.from_user.id] = res
        await callback.answer('Вы проголосовали')
    else:
        await callback.answer('Вы уже проголосовали! Больше нельзя',
                              show_alert=True)



executor.start_polling(dp, skip_updates=True)



'''CallbackQuery - это класс,который возвращает объект запросаобратного 
вызова в ответ на некоторые события. Имеет множество атрибутов. При этом у 
конкретного объекта CallbackQuery будет: уникальный идентификатор(id:str) 
который формируется telegram API при генерации данногозапроса у нас будет 
объект юзера(from:user) будет объект message:Message ,сообщение  к которому 
была прикреплена онлайн кнопка, онлайн клавиатура ,будут некоторые данные(
data:str), которые мы будем отправлять в нашем call back запросе и так далее 
и вот наш объект callback является экземпляром класса CallbackQuery(
callback: types.CallbackQuery)  и хранит в себе данные сгенерированного 
запроса обрабатывается посредством объекта callback_query_handler это 
декоратор хендлер использующийся для реализации обработки объекта запроса. 
Декоратор хендлер обрабатывает ни одно а множество объектов CallbackQuery . 
Для избирательной обработки используется специальный фильтр '''
