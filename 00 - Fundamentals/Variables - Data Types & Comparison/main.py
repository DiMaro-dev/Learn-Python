# Variabiles in Python are not declared with a specific type
# They are dynamically typed, meaning the type is determined at runtime

# snake_case is the convention for variable names in Python
dummy_variable = "This is a variable"
print("Output:", dummy_variable) # Output: This is a variable

# Constants are typically defined in all uppercase letters
PI = 3.14159

# --- Data Types ---
name = "Bob"  # String variable
age = 20  # Integer variable    
height = 5.9  # Float variable
is_student = True  # Boolean variable
x, y, z = 1, 2, 3  # Multiple assignment
# x Wrong, no need declaration; x = 5  Right
l = [1, 2, 3]  # List variable
t = (1, 2, 3)  # Tuple variable
r = range(5)  # Range variable
d = {"key1": "value1", "key2": "value2"}  # Dictionary variable
s = {1, 2, 3}  # Set variable

# --- How to get the type of a variable ---
print("Type of name:", type(name))  # Output: <class 'str'>
print("Type of age:", type(age))  # Output: <class 'int'>
print("Type of l:", type(l))  # Output: <class 'list'>
print("Type of t:", type(t))  # Output: <class 'tuple'>
print("Type of d:", type(d))  # Output: <class 'dict'>
print("Type of s:", type(s))  # Output: <class 'set'>
# etc ...

# --- Printing variables ---

print("Name:", name)  # Print the name variable

name = "Alice"  # Reassigning the name variable
print("New Name:", name)  # Print the new name variable

dummy_variable = 10 # Variable can be reassigned to a different type
print("Output:", dummy_variable) # Output: 10

print(PI * y) # Output: 6.28318

# --- Comparison Operators ---
print(x == y)  # Equal to  # output: False
print(z > y)  # Greater than # output: True
print(x != z)  # Not equal to # output: True
print(x <= y)  # Less than or equal to # output: True
# etc. More comparison operators can be used similarly

