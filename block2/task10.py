chislo = int(input("введите трёхзначное число: "))
ed = chislo % 10
des = (chislo // 10) % 10
sum = chislo // 100 + des + ed
pr = chislo // 100 * des * ed
print(ed, des, sum, pr)
