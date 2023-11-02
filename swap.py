# Write a Python program to swap two variables.

name = "Python"  
year = "1995"

temp = name
name = year
year = temp

print("The name value after the swapping: {}" .format(name))
print("The year value after the swapping: {}" .format(year))

print()

# Users can also give the inputs..

name = "Python"
year = "1995"

name = input("Enter the value for name: ")
year = input("Enter the value for year: ")

temp = name
name = year
year = temp

print("The name value after the swapping: {}" .format(name))
print("The year value after the swapping: {}" .format(year))