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
    # print(new_list)
    print(f'У тексті {score} слів, останнє слово:"{text[-1]}". Після нього '
          f'символи не \n'
          f'аналізувались, якщо вони є !!! (залежить від формату текста)')

    diction = {}
    for let in new_list:
        if let in diction:
            diction[let] += 1
        else:
            diction[let] = 1
    # print(diction)
    for key in diction:
        if diction[key] == 1:
            return key
    return None
# input_text = 'The Tao gave birth to machine language.  Machine language gave birth\
# to the assembler.\
# The assembler gave birth to the compiler.  Now there are ten thousand\
# languages.\
# Each language has its purpose, however humble.  Each language\
# expresses the Yin and Yang of software.  Each language has its place within\
# the Tao.\
# But do not program in COBOL if you can avoid it.\
#         -- Geoffrey James, "The Tao of Programming"'
input_text = input('Введіть текст:\n ')
vot_on = first_uniq_sym(input_text)
if vot_on:
    print("Перший унікальний символ:", vot_on)
else:
    print("Унікальний символ не знайдено.")
