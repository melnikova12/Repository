#вариант 1

fname = input('Введите название файла: ')

#функция,которая считает сколько раз в тексте встречается слово,
#оканчивающееся на -ing
def find_ing_word():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read().lower()
    symbols_to_remove = """,.:;()-–?!*"""
    for s in symbols_to_remove:
        text = text.replace(s, '')
    words = text.split()
    m = 0
    for i in words:
        if i.endswith('ing'):
            m = m+1
    return m
print ('Количество форм на -ing: ', find_ing_word())


word = input('Введите слово, оканчивающееся на -ing: ')


#функция, которая считает сколько раз встречается в тексте слово,
#которое вводит пользователь
def user_word():
    with open (fname, encoding = 'utf-8') as f:
        text = f.read()
    text = text.lower()
    symbols_to_remove = """,.:;()-–?!*"""
    for s in symbols_to_remove:
        text = text.replace(s, '')
    words = text.split()
    m = 0
    for i in words:
        if i == word:
            m = m+1
        else:
            m = m+0
    return m
print('Количество введенного вами слова в тексте: ', user_word())
