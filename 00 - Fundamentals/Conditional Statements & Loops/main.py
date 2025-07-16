# if elif else statements

# if condition:
if True:
    print("This is true")  # This will execute
# elif condition:
elif False:
    print("This is false")  # This will not execute
# else:       
else:
    print("This is the else block") # This will not execute
# --- Indentation ---
# Python uses indentation to define blocks of code              
# Indentation is important in Python to define blocks of code
# No semicolons are needed at the end of lines in Python

x, y, z = 10, 20, 30

if x < y:
    print("x is less than y (", x, "<", y, ")")  
elif x > z:
    print("x is greater than z")
else:
    print("x is equal to y")

x, y, z = 20, 10, 15
if x > y:
    print("x is greater than y (", x, ">", y, ")")  
elif x < y:
    print("x is less than z")
else:
    print("x is equal to y")


# -- Loops ---
# for loop
print("For Loop 0 to 4:")
for i in range(5):  # Loop from 0 to 4
    print("Iteration:", i)  # Print the current iteration number
print("-----------------")

# while loop
print("While Loop count < 5")
count = 0
while count < 5:  # Loop while count is less than 5
    print("Count is:", count)  # Print the current count
    count += 1  # Increment count by 1    
print("-----------------")  

# break statement
print("For Loop break")
for i in range(10):  # Loop from 0 to 9
    if i == 5:  # If i is equal to 5
        break  # Exit the loop
    print("Current number:", i)  # Print the current number
print("-----------------")

# continue statement
print("For Loop continue")
for i in range(10):  # Loop from 0 to 9 
    if i % 2 == 0:  # If i is even
        continue  # Skip the rest of the loop for this iteration
    print("Odd number:", i)  # Print the current odd number
print("-----------------")

# pass statement
print("For Loop pass")
for i in range(5):  # Loop from 0 to 4
    if i == 2:  # If i is equal to 2
        pass  # Do nothing
    print("Current number:", i)  # Print the current number 
print("-----------------")

# Nested loops
print("Nested Loops")
for i in range(3):  # Outer loop
    for j in range(2):  # Inner loop
        print("i:", i, "j:", j)  # Print the current values of i and j, matrix style
print("-----------------")

# Looping through a list
print("Looping through a list") 
my_list = [1, 2, 3, 4, 5]  # List of numbers
for item in my_list:  # Loop through each item in the list
    print("Item:", item)  # Print the current item
print("-----------------")  

# Looping through a dictionary
print("Looping through a dictionary")
my_dict = {"a": 1, "b": 2, "c": 3}  # Dictionary to loop through
for key, value in my_dict.items():  # Loop through each key-value pair in the dictionary
    print("Key:", key, "Value:", value)  # Print the current key and value
print("-----------------")

# Looping strings, set, and tuple...