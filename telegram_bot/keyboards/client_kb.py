from aiogram.types import ReplyKeyboardMarkup, KeyboardButton  # ,

# ReplyKeyboardRemove

b1 = KeyboardButton('/Режим_работы') # Запускаем класс KeyboardButton
b2 = KeyboardButton('/Расположение')
b3 = KeyboardButton('/Меню')
b4 = KeyboardButton('Поделиться номером', request_contact=True)
b5 = KeyboardButton('Отправить где я', request_location=True)

kb_client = ReplyKeyboardMarkup(resize_keyboard=True)#.add(b1).add(b2).add(b3)
# Запускаем класс
# ReplyKeyboardMarkup,этот класс замещает клавиатуру обычную на ту, которую
# мы создаем
kb_client = kb_client.add(b1).add(b2).add(b3).row(b4, b5)  # каждая кнопка
# отдельно,сверху вниз


# kb_client = kb_client.add(b1, b2, b3) <- расположнеы в 1 ряд.row(b4,
# b5) - и эти тоже расположнеы в 1 ряд

# kb_client.add(b1).add(b2).insert(b3) # две кнопки(b2 и b3) типа в одном
# ряду
# kb_client.row(b1, b2, b3)  # row, то есть
# добавления  всех кнопок в строку.Компоновать методы и кнопки можно как угодно
# kb_client.add(b1).insert(b2).row(b3)
