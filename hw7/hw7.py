#вариант 1

fname = input('Введите название файла: ')

#функция,которя считает сколько раз в тексте встречается слово,
#оканчивающееся на -ing
def find_ing_word():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split()
        m = 0
        for i in words:
            if i.endswith('ing'):
                m = m+1
        return m
print ('Количество слов, оканчивающихся на -ing: ', find_ing_word())


#функция, которая считает сколько раз в тексте встречается слово,
#оканчивающееся на -ing, введенное пользователем

word = input('Введите слово из текста, оканчивающееся на -ing: ')

def user_word():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
        words = text.split()
        m = 0
        for i in words:
            if i == word:
                m = m+1
        return m
print('Количество введеного вами слова в тексте: ', user_word())
    
        


