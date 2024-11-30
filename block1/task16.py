from math import sin

x = int(input("введите x: "))
a = int(input("введите a: "))
b = int(input("введите b: "))
c = int(input("введите c: "))
# print(f"{a} / {b} / {c} = {a / b / c}")
# print(f"{a} * {b} / {c} = {a * b / c}")
# print(f"{a} + {b} / {c} = {a + b / c}")
# print(f"({a} + {b}) / {c} = {(a + b) / c}")
# print(f"{a} + {b} / {b} + {c} = {a + b / b + c}")
# print(f"({a} + {b}) / ({b} + {c}) = {(a + b) / (b + c)}")
print(f"{a} / sin{b} = {a / sin(b)}")
print(f"1 / 2 * {a} * {b} * sin{x} = {round(1 / 2 * a * b * sin(x)), 2}")