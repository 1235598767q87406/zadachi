chislo = int(input("введите четырёхзначное число: "))
ch4 = chislo % 10
ch3 = (chislo // 10) % 10
ch2 = (chislo // 100) % 10
ch1 = chislo // 1000
print(f"a) {ch1+ch2+ch3+ch4} b) {ch1*ch2*ch3*ch4}")
