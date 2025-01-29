import pandas as pd

myList = {
  'Names': ["Prakrit", "Sambeed", "Jeevan", "Kushal", "Arogya"],
  'Girls': [0, 0, "Infinite", 0, 1],
  'Education': ["Grade 10", "Grade 10", "Bachelors", "Grade 10", "Grade 9"]
}
myList = pd.DataFrame(myList)
print(myList)
