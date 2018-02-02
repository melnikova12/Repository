#Напишите программу, которая запрашивает у пользователя слово или фразу
#и переводит его на Pig Latin: world → orldway.

print ("Привет! Сейчас ты увидишь как работает Pig Latin")
p = input('Введите слово на английском языке: ')
consonants = 'bcdfghjklmnpqrstvwxz'
for i in range(0,len(p)):
    if p[0] in consonants:
        p = p[1:] + p[0]
print(p + "ay")
