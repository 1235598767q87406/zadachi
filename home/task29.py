n = int(input("введите число от 10 до 999: "))
if n < 10 or n > 999:
    print("вы ввели недопустимое число")
else:
    ch1 = n % 100 // 10
    ch2 = n // 100
    ch3 = n % 10
    print(f"{ch1}{ch2}{ch3}")
