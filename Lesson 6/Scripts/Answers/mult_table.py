# Таблица умножения от 1 до 10
i = 1
while i <= 10:
    j = 1
    while j <= 10:
        #print("{0: =3}".format(j * i), end=" ")
        print(str(j * i).rjust(3, ' '), end=" ")
        j += 1
    i += 1
    print()
