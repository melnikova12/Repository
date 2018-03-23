#вариант 1 
#В этом домашнем задании программа должна открывать файл с русским текстом
#в кодировке UTF-8 и распечатывать из него по одному разу
#все встретившиеся в нём формы глагола «открыть»

#В формы глагола включаются деепричастия,
#причастия и формы на -ся и не включаются видовые пары.
#И особое внимание стоит уделить тому, чтобы программа ничего,
#кроме форм этих глаголов, не распознавала.


import re

fname = input ('Введите название файла: ')

with open (fname, encoding = 'utf-8') as f:
    text = f.read().lower()
    symbols_to_remove = """,.:;()-–?!*"""
    for s in symbols_to_remove:
        text = text.replace(s, '')

def find_forms():
    forms = re.findall(r'откры[ть,л,ла,ло,вает,вающий,вающее,вающая,вшийся,вшаяся,вшееся]*',text)
    return forms

def print_match():
    print ('Формы глагола «открыть» в вашем тексте: ')
    for match in find_forms():
        print (match)

print_match()
