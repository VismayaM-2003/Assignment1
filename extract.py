# Write a Python program to extract a single key-value pair from a dictionary into variables.

college = {
    
    "year": 2023,
}

print("Dictionary is: ", college)

key, value = next(iter(college.items()))

print("The key is: ", key)
print("The value is: ", value)

