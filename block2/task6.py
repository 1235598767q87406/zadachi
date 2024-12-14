sec = int(input("сколько сек прошло с начала суток? "))
hours = sec // 3600
min = (sec - hours * 3600) // 60
sec1 = sec - hours * 3600 - min * 60
print(f"{hours} часов, {min} минут, {sec1} секунд")
