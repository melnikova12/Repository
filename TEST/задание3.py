
#задание 3
#Программа должна спрашивать у пользователя названия языков, пока тот не введёт пустое слово.
#После этого она должна для каждого языка распечатать через тире а) само название языка, б) число говорящих, в) статус языка.
#Если название не встретилось в списке, то нужно вывести сообщение о том, что языка в списке нет.


with open("Extinct_languages.tsv", encoding="utf-8") as f:
    lines = f.readlines()
    word = input("Пожалуйста, введите название языка: ")
    all_words = []
    while word != '':
        all_words.append(word)
        word = input ("Пожалуйста,введите еще одно название языка: ")
    splitted_lines = []
    for line in lines:
        line_stop = line.strip()
        splitted_lines.append(line_stop.split('\t'))
    for word in all_words:
        print(word)
        log = True   #что-то вроде переключателя
        for one_line in splitted_lines:
            if word == one_line[0]:
                print("количество говорящих на языке:", one_line[1], ", cтатус языка:", one_line[2])
                log = False
        if log == True:
           print("Язык не найден")


#я не поняла, почему у меня результат выводится в итоге 2 раза :(
