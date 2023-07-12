import json

# ar = []
with open('cenz.txt', encoding='utf-8') as r:
    ar = r.read().lower().split()
    # for i in r:
    #     print(i)
    #     n = i.lower().split('\n')[1]
    #     # n = i.lower().replace('\n', '')
    #     print(n)
    #     # if n != '':
    #     ar.append(n)
    # print(ar)

with open('cenz.json', 'w', encoding='utf-8') as e:
    json.dump(ar, e)
'''используем из модулей json функцию dump, который позволяет нам записать
данные в этот джейсон файл. Передаем туда как первый аргумент наш список из
слов и передаем туда непосредственно сам объект чтения(е) '''
