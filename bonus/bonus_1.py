k = input ('Введите число: ')
m = []
a = []
m.append(k)
while k != '':
    k = input ('Введите число: ')
    m.append(k)
m.pop()   #удаляет последний элемент - пустую строку
for i in m:
    a.append(int(i))
print('Максимальное число: ', max(a))
print ('Минимальное число: ', min(a))
average = sum(a)/len(a)
print('Среднее арифметическое:', average)
    
    
