# Write a Python program to check whether lowercase letters exist in a string.


text = "she exercises every morning."

# It will check the all characters in the string is lowercase or not..

result = text.islower() 

print(result)

if result:
    
    print("Lowercase letters exist in a given string..")
    
else:
    
    print("Lowercase letters are not exist in a given string..")