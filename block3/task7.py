a = True
b = False
c = False
print(f"1) {a or not (a and b) or c}\n2) {not a or a and (b or c)}\n\
3) {(a or b and not c) and c}")
