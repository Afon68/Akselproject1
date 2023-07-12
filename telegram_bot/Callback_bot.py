from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
# from aiogram.dispatcher import Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton
from aiogram.dispatcher.filters import Text

# from aiogram.utils import executor
# from aiogram.dispatcher.filters import Text

bot = Bot(token='5935424823:AAEQYLYpI-xEF5JqtTgUvC71VUhzu865w3I')  #
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/vote')
kb.add(b1, b2)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Welcome to our bot', reply_markup=kb)


@dp.message_handler(commands=['vote'])
async def vote_command(message: types.Message):
    ikb = InlineKeyboardMarkup(row_width=2)
    ib1 = InlineKeyboardButton(text='❤️', callback_data='yes like')
    ib2 = InlineKeyboardButton(text='👎', callback_data='dis like')
    ikb.add(ib1, ib2)
    await bot.send_photo(chat_id=message.from_user.id,
                         photo='https://onefield.in/wp-content/uploads/2021/03/lemon100g.jpg',
                         caption='Нравится фотка?', reply_markup=ikb)


answ = dict()


@dp.callback_query_handler((Text(endswith='like')))
async def vote_callback(callback: types.CallbackQuery):
    count_like = 0
    # count_dislike = 0
    res = callback.data.split()[0]
    if callback.from_user.id not in answ:
        answ[callback.from_user.id] = res
        count_like += 1
        await callback.answer(f'Вы проголосовали!У нас { count_like} like',
                              show_alert=True)
    else:
        await callback.message.answer('Вы уже проголосовали! Больше нельзя!')
        await callback.answer('Вы уже проголосовали! Больше нельзя!',
                              show_alert=True)


    # count_like = 0
    # count_dislike = 0
    # if callback.data == 'yes like':
    #     count_like += 1
    #     await callback.answer(text=f'Super!У нас уже {count_like} like ',
    #                           show_alert=True)
    # count_dislike += 1
    # await callback.answer(f"You don't like 😢 ?\n "
    #                       f"У нас к сожалению {count_dislike} dislike ",
    #                       show_alert=True)



