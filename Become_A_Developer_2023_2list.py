
'''Вам потрібно розробити алгоритм програми, яка повинна виконувати
наступне: - програма приймає на вхід довільний текст і знаходить в кожному
слові цього тексту найперший символ, який більше НЕ повторюється в
аналізуємому слові - далі із отриманого набору символів програма повинна
вибрати перший унікальний (тобто той, який більше не зустручається в наборі)
і повернути його. '''

def first_uniq_sym(words):
    score = 0
    text = words.split()
    new_list = []
    for el in text:
        score += 1
        for sym in el:
            if el.count(sym) == 1:
                new_list.append(sym)
                break
    print(f'У тексті {score} слів, останнє слово:"{text[-1]}". Після нього '
          f'символи не \n'
          f'аналізувались, якщо вони є !!! (залежить від формату текста)')
    for let in new_list:
        if new_list.count(let) ==1:
            return let
    return None
input_text = 'The Tao gave birth to machine language.  Machine language gave birth\
to the assembler.\
The assembler gave birth to the compiler.  Now there are ten thousand\
languages.\
Each language has its purpose, however humble.  Each language\
expresses the Yin and Yang of software.  Each language has its place within\
the Tao.\
But do not program in COBOL if you can avoid it.\
        -- Geoffrey James, "The Tao of Programming"'
# input_text = input('Введіть текст:\n ')
vot_on = first_uniq_sym(input_text)
if vot_on:
    print("Перший унікальний символ:", vot_on)
else:
    print("Унікальний символ не знайдено.")

# for letter in char_count:
#     if char_count[letter] == 1:
#         unique_chars.append(letter)

x ={9, 8, 7, 6, 9, 5, 7, 8, 6, 5}
print(type(x))

y = list(range(5000, 5005))
print(y)