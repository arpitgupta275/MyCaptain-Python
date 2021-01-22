# Python Program to Print Positive Numbers in a List

NumList = []
Positives = []

Number = int(input("Please enter the Total Number of List Elements: "))
for i in range(1, Number + 1):
    value = int(input("Please enter the Value of %d Element : " %i))
    NumList.append(value)

for j in range(Number):
    if(NumList[j] >= 0):
      Positives.append(NumList[j])

print(Positives)
