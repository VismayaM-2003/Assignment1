# Write a Python program to calculate the sum of all items of a container (tuple, list, set, dictionary)

print("The sum of all items of a container (tuple, list, set, dictionary)..")

# Tuples

# Calculate the  sum of all items in the given Tuple. 

data_1 = sum((10, 20, 30, 40, 10))

print("Tuple: ", data_1)



# List

# Calculate the  sum of all items in the given List. 

data_2 = sum([100, 200, 300, 400, 100])
     
print("List: ", data_2)



# Set

# Calculate the  sum of all items in the given Set.

data_3 = sum({1, 2, 3, 4, 5, 1})   

print("Set: ", data_3)




# Dictionary

def sum(data_4):
    sum = 0
    
    for x in data_4:
        sum = sum + data_4[x]
        
    return sum

data_4 = {
    'num1': 1, 
    'num2': 2, 
    'num3': 1, 
    'num2': 2
    }

# Calculate the  sum of all items in the given Dictionary. 

result = sum(data_4)       


print("Dictionary: ", result)


