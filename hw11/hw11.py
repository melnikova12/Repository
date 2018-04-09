#вариант 1
#статья "комар", заменить "комар" на "слон"

#этот код работает с файлами формата .txt

import re


def file():
    with open ('комар.txt', 'r',  encoding = 'utf-8') as f:
        text = f.read()
    return text 

def change(text):
    first = re.sub('комар', 'слон', text)
    second = re.sub('комары', 'слоны', first)
    third = re.sub('комаров','слонов', second)
    fourth = re.sub('комара', 'слона', third)
    fifth = re.sub('комарами', 'слонами', fourth)
    six = re.sub ('комарах', 'слонах', fifth)
    seven = re.sub ('комаром','слоном', six)
    eight = re.sub ('комару', 'слону', seven)
    nine = re.sub ('Комары', 'Слоны', eight)
    ten = re.sub ('Комар', 'Cлон', nine)
    return ten

def write_in_file(ten):
    with open ('text.txt', 'w', encoding = 'utf-8') as f:
        f = f.write(ten)

def final():
    text = file()
    write_in_file(change(text))

final()
