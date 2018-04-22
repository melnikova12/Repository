#вариант 1 
import os
import re

print ('Данная программа показывает сколько найдено папок, содержащих цифры в названии')

def find_folders():
    i = 0
    path = '../Documents'
    if os.path.exists(path):
        print ('Все верно,данный путь существует.')
    else:
        print('Что-то пошло не так :(')
    path = os.listdir()
    for folder in path:
        #if os.path.exists(folder):
        if os.path.isdir(folder):
            if re.findall('.?[0-9].?', folder):
                i = i+1
              #  continue
       # if os.path.isdir(folder):
       #     if re.findall('.?[0-9].?', folder):
       #         i = i+1
    print ('Папок, в названии которых содержатся цифры: ', i )

find_folders()
