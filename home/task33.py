n = int(input("введите число от 1 до 999: "))
if n < 1 or n > 999:
    print("вы ввели недопустимое число")
else:
    ch1 = n // 100
    ch2 = n % 100 // 10
    ch3 = n % 10
    print(f"x = {ch3}{ch2}{ch1}")
