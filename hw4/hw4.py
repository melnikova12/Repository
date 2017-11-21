#вариант 1 - найти среднее число слов в строке

with open("/Users/melnikovaarina/Desktop/stranger_things.txt",
          encoding="utf-8") as f:
    text = f.read()
text = text.replace("\ufeff","")

lines = text.splitlines()

al = 0
st = 0
for x in lines:
    st += 1
    length = len(x.split())
    al += length
    
print("Среднее число слов в строке: ", int(al/st))
