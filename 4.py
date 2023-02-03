#1 Arrays

"""
List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.
"""


cars = ["Ford", "Volvo", "BMW"]

x = cars[0]
print(x)

cars[0] = "Toyota"
x = len(cars)
print(x)

for x in cars:
  print(x)

cars.append("Honda")
cars.pop(1)
