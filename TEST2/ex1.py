#вариант 2 
#1. (5 баллов) Открыть файл и посчитать число символов внутри тега body,
#то есть между строками <body> и </body>, открыть другой файл и записать туда
#число подсчитанных символов.

import re 

fname = input ('Введите название файла: ')

#чтение файла
with open (fname, encoding = 'utf-8') as f:
    f = f.read()
    
#поиск символов
search = re.findall(r'<w>.*</w>', f)

#запись в файл
#файл для записи -  text.txt
with open ('text.txt', 'w', encoding = 'utf-8') as f:
    f = f.write(str(len(search)))                   
