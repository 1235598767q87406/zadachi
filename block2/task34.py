num1 = input("введите двузначное число: ")
num2 = input("введите однозначное число: ")
a1 = num1[1]
a2 = num1[0]
b = num2[0]

if a1 == "0":
    print(f"{a2}{b}")
elif a1 == "1" and b == "1":
    print(f"{a2}2")
elif a1 == "1" and b == "2" or a1 == "2" and b == "1":
    print(f"{a2}3")
elif a1 == "1" and b == "3" or \
    a1 == "3" and b == "1" or \
        a1 == "2" and b == "2":
    print(f"{a2}4")
elif a1 == "4" and b == "1" or a1 == "1" and b == "4":
    print(f"{a2}5")
elif a1 == "3" and b == "2" or a1 == "2" and b == "3":
    print(f"{a2}5")
elif a1 == "5" and b == "1" or a1 == "1" and b == "5":
    print(f"{a2}6")
elif a1 == "2" and b == "4" or \
    a1 == "2" and b == "3" or \
        a1 == "3" and b == "3":
    print(f"{a2}6")
elif a1 == "5" and b == "2" or a1 == "2" and b == "5":
    print(f"{a2}7")
elif a1 == "4" and b == "3" or a1 == "3" and b == "4":
    print(f"{a2}7")
elif a1 == "3" and b == "5" or \
    a1 == "5" and b == "3" or \
        a1 == "4" and b == "4" or \
        a1 == "6" and b == "2" or \
        a1 == "2" and b == "6" or \
        a1 == "1" and b == "7" or \
        a1 == "7" and b == "1":
    print(f"{a2}8")
elif a1 == "5" and b == "4" or \
    a1 == "5" and b == "4" or \
    a1 == "1" and b == "8" or \
    a1 == "8" and b == "1" or \
    a1 == "7" and b == "2" or \
        a1 == "2" and b == "7" or \
        a1 == "6" and b == "3" or \
        a1 == "3" and b == "6":
    print(f"{a2}9")
elif int(a1) + int(b) >= 10:
    if a2 == "1":
        print(f"2{(int(a1) + int(b)) % 10}")
    if a2 == "2":
        print(f"3{(int(a1) + int(b)) % 10}")
    if a2 == "3":
        print(f"4{(int(a1) + int(b)) % 10}")
    if a2 == "4":
        print(f"5{(int(a1) + int(b)) % 10}")
    if a2 == "5":
        print(f"6{(int(a1) + int(b)) % 10}")
    if a2 == "6":
        print(f"7{(int(a1) + int(b)) % 10}")
    if a2 == "7":
        print(f"8{(int(a1) + int(b)) % 10}")
    if a2 == "8":
        print(f"9{(int(a1) + int(b)) % 10}")
    if a2 == "9":
        print(f"10{(int(a1) + int(b)) % 10}")
else:
    print("что-то пошло не так")
