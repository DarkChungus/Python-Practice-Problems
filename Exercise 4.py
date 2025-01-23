limit, a, b = int(input("Enter the limit for the fibonacci sequence: ")), 0, 1
for i in range(1, limit): print(b); c = a + b; a = b; b = c
