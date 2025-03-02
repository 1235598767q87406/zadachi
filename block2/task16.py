chislo = int(input("введите трёхзначное число: "))
if chislo < 100:
    print("ошибка")
if chislo > 1000:
    print("ошибка")
else:
    ch1 = chislo % 10
    ch2 = chislo // 100
    ch3 = chislo // 10 % 10
    print(f"{ch1}{ch3}{ch2}")
