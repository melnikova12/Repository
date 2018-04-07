#вариант 2 
#1. (5 баллов) Открыть файл и посчитать число символов внутри тега body,
#то есть между строками <body> и </body>, открыть другой файл и записать туда
#число подсчитанных символов.

import re 

fname = input ('Введите название файла: ')

with open (fname, encoding = 'utf-8') as f:
    text = f.read()

search = re.findall(r'<w>.*</w>', text)


file = input('Введите название файла, в который нужно записать информацию: ')
with open (file, 'w', encoding = 'utf-8') as f:
    f = f.write(str(len(search)))                   
