n = int(input("введите число от 100 до 999: "))
if n < 100 or n > 999:
    print("вы ввели недопустимое число")
else:
    ch1 = n % 100 // 10
    ch2 = n // 100
    ch3 = n % 10
    print(f"{ch2}{ch3}{ch1}")
