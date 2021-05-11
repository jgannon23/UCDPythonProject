# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
#Addition
print(7 + 5)
print(5 / 8)
print(5 - 5)
print(3 * 5)
print(10 / 2)
print(18 % 7)
print(4 ** 2)

savings = 100
print(savings)

growth_multiplier = 1.1

result = savings * growth_multiplier ** 7
print(result)

# Create a variable desc
desc = "compound interest"

# Create a variable profitable
import pandas as pd

data=pd.read_csv("world-happiness-report-2021.csv")

print(data.info())
print(data.describe())


# Fix the printout
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
pi_float = float(pi_string)
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv], ["bedroom", bed], ["bathroom", bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))



