#вариант 1
#нужно, чтобы программа открывала заранее сохраненный файл html
#(статья о какой-то стране) и записывала в отдельный текстовый файл столицу

import re

def open_page():
    with open ('испания1.html', encoding = 'utf-8') as f:
        page = f.read()
    return page

def write(page):
    s = re.search(r'<dd>Столица-<br>(.*?)</dd>', page)
    return s
    with open ('text.txt', encoding = 'utf-8') as f:
        f.write(s)

page = open_page()
print(write(page))
                

#что мертво, умереть не может!
#p.s. ну хотя бы ошибку не выдает :)
