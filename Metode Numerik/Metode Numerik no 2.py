import math as mt
sqrt = mt.sqrt

print("Memasukkan variabel a")
a = float(input())
print("Memasukkan variabel b")
b = float(input())
print("Memasukkan variabel c")
c = float(input())
d = b ** 2 - 4 * a * c
if d >= 0:
    print("akar akar persamaan yakni")
    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    print("x1 = " + str(x1) + " dan x2 = " + str(x2))
else:
    print("akar akar persamaan imaginer")
