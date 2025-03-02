chislo = input("введите трёхзначное число: ")
dlina = len(chislo)
if dlina < 3:
    print("ошибка")
if dlina > 4:
    print("ошибка")
else:
    print(f"{chislo[0]}{chislo[2]}{chislo[1]}")
