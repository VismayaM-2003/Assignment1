# Write a Python program to create a histogram from a given list of integers.

number = int(input("Enter a number: "))

# Convert the number to a string
number_str = str(number)

# Print each value repeated the same number of times as itself
for value in number_str:
    repeat_digit = int(value) * str(value)
    
    print(repeat_digit)
