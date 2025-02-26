import math
n,mod = int(input(""))
F_n = int((1/math.sqrt(5))*((((1+math.sqrt(5))/2)**n)-(((1-math.sqrt(5))/2)**n)))
print(F_n)
