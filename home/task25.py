n = int(input("введите число "))
if n < 10 or n > 1000:
    print("ошибка")
else:
    ch1 = n % 100
    ch2 = ch1 * 10
    ch3 = ch2 + (n // 100)
    print(f"x = {ch3}")
