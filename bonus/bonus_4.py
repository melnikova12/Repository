# Aigy Paigy: программа запрашивает у пользователя слово или фразу и переводит
#его на "кирпичный" язык  - после каждой гласной добавляется "с" и та же гласная

word = input ("Введите слово: ")
vowels = "аеёиоуэюя"
for i in word:
    if i in vowels:
        i = i + "с" + i
        print (i, end = "")
    else:
        print (i, end = "")





        