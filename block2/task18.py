chislo = int(input("введите трёхзначное число: "))
ch3 = chislo % 10
ch1 = chislo // 100
ch2 = chislo // 10 % 10
if ch1 == ch2 or ch2 == ch3:
    print("ошибка")
else:
    print(f"{ch3}{ch2}{ch1}, {ch2}{ch3}{ch1}, {ch1}{ch3}{ch2}, {ch3}{ch1}{ch2}\
          {ch2}{ch1}{ch3}")
