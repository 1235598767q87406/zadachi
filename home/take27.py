n = int(input("введите число от 1 до 999: "))
if n < 1 or n > 999:
    print("вы ввели недопустимое число")
else:
    ch1 = n % 100
    ch2 = ch1 * 10
    result = ch2 + (n // 100)
    print(f"x = {result}")
