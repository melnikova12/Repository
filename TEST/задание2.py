#вариант1

#задание 2
#Программа должна посчитать число языков в списке,
#статус которых определён как "Critically endangered"

with open ("Extinct_languages.tsv", encoding="utf-8") as f:
    lines = f.readlines()
    i = 0  #переменная для подсчета количества строк
    for line in lines:
        if "Critically endangered" in line:
            i += 1
    print ("Число языков: ", i)

    
