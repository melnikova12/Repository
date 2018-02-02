#Aigy Paigy: пользователь вводит английское слово или фразу,
#программа вставляет после каждого согласного
#“aig”: “Hello girl!” → “Haigelaigo gaigirl!

word = input ("Введите слово или фразу строчными буквами на латинице: ")
cons = "bcdfghjklnmpqrstvwxz"
for i in word:
    if i in cons:
        i = i + "aig" 
        print (i, end = "")
    else:
        print (i, end = "")


#кстати в примере ошибка: должно быть не “Haigelaigo gaigirl!",
         #а  "haigelaiglaigo gaigiraiglaig"
