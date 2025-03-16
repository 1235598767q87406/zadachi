chislo = int(input("введите четырёхзначное число: "))
ch4 = chislo % 10
ch3 = chislo // 10 % 10
ch2 = chislo // 100 % 10
ch1 = chislo // 1000
print(f"a) {ch4}{ch3}{ch2}{ch1} b) {ch2}{ch1}{ch4}{ch3}")
print(f"c) {ch1}{ch3}{ch2}{ch4} d) {ch3}{ch4}{ch1}{ch2}")

chislo_str = str(chislo)
print(f"{chislo_str[2:]}{chislo_str[:2]}")
