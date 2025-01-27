import math

def permutation(n, r):
  return math.factorial(n)/math.factorial(n-r)

def combination(n, r):
  return math.factorial(n)/math.factorial(r)*math.factorial(n-r)


userInput = int(input("Enter 1 for permutation and 2 for combination: "))
if userInput == 1:
  print("     n!     ")
  print("------------")
  print("( n  -  r )!")
  n = int(input("Enter n: "))
  r = int(input("Enter r: "))
  print(f"Permutation is {permutation(n,r)}")
elif userInput == 2:
  print("       n!     ")
  print("--------------")
  print("r!( n  -  r )!")
  n = int(input("Enter n: "))
  r = int(input("Enter r: "))
  print(f"Combination is {combination(n,r)}")
else:
  print("Invalid Input! Sorry!")
