def isPalin(n):
    if str(n)[::-1]==str(n):
        return True


n = int(input("Enter any number to check if it is a palindrome: "))
if isPalin(n):
    print(f'{n} is a palindrome!')
else:
    print(f'{n} is not a palindrome!')
