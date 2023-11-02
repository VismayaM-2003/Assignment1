# Write a Python program to test if a variable is a list, tuple, or set.

# Testing For Tuples

task_1 = (1, 2, 3, 4, 5, 6, 7)

test_1 = "True, The given variable is a Tuple.." if type(task_1) == tuple else "False, The given variable is not a Tuple.." 

print(test_1)


# Testing For List

task_2 = ["python", "C", "C++", "Java"]

test_2 = "True, The given variable is a List.." if type(task_2) == list else "False, The given variable is not a List.." 

print(test_2)


# Testing For Set

task_3 = {100, 200, 300, 400, 500}

test_3 = "True, The given variable is a Set.." if type(task_3) == set else "False, The given variable is not a Sett.." 

print(test_3)



