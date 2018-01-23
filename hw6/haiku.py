#Вариант 1
#Текст должен представлять собой правильное хайку,
#то есть стихотворение на русском языке из трёх строк без рифмы,
#при этом длина первой строки должна быть 5 слогов, второй строки - 7 слогов,
#третьей строки - 5 слогов.
#Количество предложений в таком тексте может быть любым


import random


#вызывает существительные женского рода с 2 слогами
def dva_sloga():
    with open('sloga2.txt', 'r', encoding = 'utf-8') as f:
        sloga2 = f.readlines()
    return random.choice(sloga2).replace("\n","")

#вызывает существительные женского рода с 2 слогами (для разнообразия)
def dva_sloga2():
    with open('sloga2_2.txt', 'r', encoding = 'utf-8') as f:
        sloga2_2 = f.readlines()
    return random.choice(sloga2_2).replace("\n","")

#вызывает сущ. с 2 слогами в генетиве
def gen():
    with open('sloga2_gen.txt', 'r', encoding = 'utf-8') as f:
        sloga2_gen = f.readlines()
    return random.choice(sloga2_gen).replace("\n","")


#вызывает сущ.  с 2 слогами в генетиве (для разнообразия)
def gen2():
    with open('sloga2_gen2.txt', 'r', encoding = 'utf-8') as f:
        sloga2_gen2 = f.readlines()
    return random.choice(sloga2_gen2).replace("\n","")


#вызывает прилагательные м.р. с 2 слогами
def adv():
    with open('adv_sloga2.txt', 'r', encoding = 'utf-8') as f:
        adv_sloga2 = f.readlines()
    return random.choice(adv_sloga2).replace("\n","")


#вызывает глаголы с 3 слогами (ж.р.)
def tri_sloga():
    with open('sloga3.txt', 'r', encoding = 'utf-8') as f:
        sloga3 = f.readlines()
    return random.choice(sloga3).replace("\n","")


#вызывает существительные м.р. с 3 слогами 
def tri_sloga2():
    with open('sloga3_2.txt', 'r', encoding = 'utf-8') as f:
        sloga3_2 = f.readlines()
    return random.choice(sloga3_2).replace("\n","")


#вызывает существительные м.р. или ср.р. с 5 слогами
def pyat_slogov():
    with open('slogov5.txt', 'r',encoding = 'utf-8') as f:
        slogov5 = f.readlines()
    return random.choice(slogov5).replace("\n","")


#пунктуация (не стала делать отдельный файл, чтобы не перегружать код)
def punctuation():
    marks = [".", "?", "!", "..."]
    return random.choice(marks)



#создаём разные варианты строчек

#вариант для строчки 1 
#сущ. ж.р. + глагол ж.р.   
def verse1():
    return dva_sloga() + ' ' + tri_sloga() + punctuation()


#два варианты для второй строчки:
# 1) сущ. ж.р. + глагол ж.р. + сущ. в генетиве  
def verse2():
    return dva_sloga() + ' ' + tri_sloga() + ' ' + gen2() + punctuation()
# 2) сущ. м.р. или ср.р.  + сущ. в генетиве
def verse3():
    return pyat_slogov() + ' ' + gen() + punctuation() 


#два варианта для 3 строчки
# 1) сущ ж.р. + глагол ж.р
def verse4():
    return dva_sloga2() + ' ' + tri_sloga() + punctuation() 
# 2) сущ.м.р. + прилаг.м.р.
def verse5():
    return tri_sloga2() + ' ' + adv() + punctuation() 



#функция выбирает случайный номер и возвращает соответствующую строчку 
def make_verse1():
    verse = random.choice([0,1])
    if verse == 0:
        return verse1()
    else:
        return verse5()
def make_verse2():
    verse = random.choice([5,6])
    if verse == 5:
        return verse2()
    else:
        return verse3()
def make_verse3():
    verse = random.choice([7,8])
    if verse == 7:
        return verse4()
    else:
        return verse4()
       
print (make_verse1())
print (make_verse2())
print (make_verse3())
   
    













