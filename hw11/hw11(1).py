#вариант 1
#статья "комар", заменить "комар" на "слон"

import re

print ("Эта программа заменяет в статье из Вики про комаров все формы слова "комар" на формы слова "слон".")
a = input('Чтобы узнать, что вам нужно сделать, введите "указания": ')
if a == 'указания':
    print ('Скачайте статью про комаров (название файла - 'комар.html') и создайте файл для записи результата 'text.html'')
else:
    print ('Скачайте статью про комаров (название файла - 'комар.html') и создайте файл для записи результата 'text.html'')
   
def file():
    with open ('комар.html', 'r',  encoding = 'utf-8') as f:
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
    with open ('text.html', 'w', encoding = 'utf-8') as f:
        f = f.write(ten)

def final():
    print ('Все готово! Статья изменена, откройте файл 'text.html' для просмотра')
    text = file()
    write_in_file(change(text))

final()
