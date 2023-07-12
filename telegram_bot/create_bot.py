from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()   # запуск класса MemoryStorage(о нем написано ниже)

# bot = Bot(token=os.getenv('TOKEN'))# инициализируем нашего бота
bot = Bot(token='5935424823:AAEQYLYpI-xEF5JqtTgUvC71VUhzu865w3I') # запуск
# класса Bot,в параметре token из telegram - BotFather?(надеюсь ,что так)
dp = Dispatcher(bot, storage=storage)  # необходимо запустить класс Dispatcher
#  и передать экземпляр нашего бота (bot)
#  Там где у нас запуск
# класса диспетчер, в которой мы передаем класс бота, дописываем следующую
# строчку, в параметр storage передаем наш экземпляр MemoryStorage ,
#  место, где мы будем хранить полученные ответы от пользователя.

'''                 МАШИНА СОСТОЯНИЙ      '''
'''Переходим к ней для чего это нужно конкретно в нашем боте,где все дело в 
том, что все хэндлеры, команды, которые есть у бота, бот не понимает разницы 
к примеру какая сработала первая, какая вторая, ему все равно он как 
болванчик , то есть режим работы нажали, расположение нажали, для него это 
никак не взаимосвязанные вещи вообще. Ну очень часто необходимо провести 
некое анкетирование, то есть к примеру загрузка меню для пиццерии нашим 
пользователям, то есть он для начала отправляет фотографию  какой-либо 
пиццы и потом записывает название, потом записывает описание и указывает 
соответственно цену. Бот  должен запомнить для того, чтобы мы потом это 
использовали, то есть отправили в базу данных и потом по кнопке 'меню', 
посетитель этой пиццерии, чтобы ему из базы данных подтягивалось все то, что 
написал администратор. Вот для чего нужна машина состояний и переходим к 
разбору кода, напоминаю, что мы пишем бота при помощи модульной системы, у нас 
есть 2 основных файла - это файл create_bot в котором создается экземпляр 
бота, 
файл входа bot_telegram, то есть который непосредственно запускается для старта
полинга и у нас есть папка handlers ,то есть пакет с хендлерами 
админа клиента и общие и пакет с клавиатурами (папка keyboards)
   Так как машина состояний позволяет задать пользователю ряд 
   взаимосвязанных вопросов и запомнить
ряд ответов от пользователя, необходимо указать хранилище в котором
бот будет хранить эти данные, грубо говоря то место,  где он
это все запомнит  from aiogram.contrib.fsm_storage.memory import MemoryStorage

       Импортируем класс MemoryStorage -
этот класс позволяет сохранить данные в 
оперативной памяти aiogram поддерживает также еще несколько хранилищ,
которые основаны уже на базах данных - это база данных mongo и а и redis, 
когда какую использовать? MemoryStorage
является самой простой,то есть храниться все это в памяти значит дело в том 
что если вам необходимо прописать машины состояний, то есть запоминать 
последовательность ответов или действий пользователя с очень важной 
информацией, например какая либо покупка или есть банковские 
данные ,то тогда необходимо использовать какую-либо из-за файловых хранилищ 
то есть базы данных редис или манга. Так как если к примеру, во время хранения 
полученных данных от пользователя, бот вылетит, то есть выйдет в в офлайн, 
данные из памяти потеряются, если они хранятся в файловой базе данных, то 
соответственно выйдя в онлайн опять, бот дальше продолжит с ним работать, но 
если вы полученные данные сразу же отправляете в обработку, например пишите в 
какую-то другую б.д. то в таком случае, вот этого простого 
хранилища(MemoryStorage), то есть оперативной памяти, вполне достаточно'''