n = int(input("введите число "))
ch1 = n % 100
ch2 = ch1 * 10
ch3 = ch2 + (n // 100)
print(f"x = {ch3}")
