#вариант1

#задание1
#Программа должна открыть список языков в кодировке UTF-8 и
#вывести на экран все записи (строки) длиннее 35 символов.

with open ("Extinct_languages.tsv", encoding="utf-8") as f:
    lines = f.readlines()
    for line in lines:
        if len(line) > 35:
            print (line)
