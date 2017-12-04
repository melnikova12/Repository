m = input("Введите слово: ")
list =[]
if m == "":
    print("Беда...")
else:
    while m != "":
        list.append(m)
        m = input("Введите слово: ")

    with open ("onegin.txt", "w", encoding="utf-8") as f:
        for i in range(len(list)):
            w = list[i]
            u = ""
            for j in range(len(w) - 1, -1, -1):
                u = u + w[j]
            for j in range(len(u)):
                if ((j + 1) % 3) != 0:
                    f.write(u[j])
            f.write("\n")
