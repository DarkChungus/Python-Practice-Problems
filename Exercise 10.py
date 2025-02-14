def sumDigit(n):
    sum = 0
    for i in range(1, len(str(n))+1):
        sum += int(str(n)[i-1])
    return sum
print(sumDigit(2**1000))
