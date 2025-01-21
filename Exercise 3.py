def fibonacci(limit):
    a, b = 0, 1
    fibonacciList = []
    for i in range(1, limit+1):
        fibonacciList.append(b)
        c = a + b
        a = b
        b = c
    print(fibonacciList)


limit = int(input("Enter how many terms of the Fibonacci sequence you want: "))
fibonacci(limit)
