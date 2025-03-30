x = False
y = False
z = True
print(f"1) {x or y and not z}\n2) {not z and not y}\n3) {not (x and z) or y}\n\
4) {x and not y or z}\n5) {x and (not y or z)}\n6) {x or (not y or z)}")
