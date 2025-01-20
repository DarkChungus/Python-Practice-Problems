# Take a list, and write a program that makes another list that has all the elements of the first list that are less than a certain number.
list = []
newList = []
limit = int(input("Enter the limit for the list that you want to go through: "))
for i in range(1, (limit+1)):
    tempNum = int(input("Enter the first element: "))
    list.append(tempNum)
checkingNumber = int(input("Enter the number you want to check the list of array with: "))
for i in range(0, limit):
    if list[i] < 5:
        newList.append(list[i])
print(f"The new list is: {newList}")
