#Напишите программу, которая запрашивает у пользователя слово или фразу
#и переводит его на Pig Latin: world → orldway.

print ("Привет! Сейчас ты увидишь как работает Pig Latin")
s = input('Введите слово на английском языке: ')
consonants = 'bcdfghjklmnpqrstvwxz'
for i in range(0,len(s)):
    if s[0] in consonants:
        s = s[1:] + s[0]
print(s + "ay")
