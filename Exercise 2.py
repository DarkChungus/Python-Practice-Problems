divisorsList = []
number = int(input("Enter any number: "))
for i in range(1, int(number/2)+1):
    if number%i==0:
        divisorsList.append(i)
divisorsList.append(number)
print(f"The list of divisors of your number is {divisorsList}")
