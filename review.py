# This program reviews the very beginning Python concepts
# No functions, loops, or conditionals are used

# Print a welcome message to the screen
print("Welcome to the Python Basics Review Program!\n")

# ---------------------------
# VARIABLES AND DATA TYPES
# ---------------------------

# String variable (text)
name = "Alice"

# Integer variable (whole number)
age = 25

# Float variable (decimal number)
height = 5.6

# Boolean variable (True or False)
is_student = True

# Print the values stored in each variable
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# 📝 Practice: Try changing the values of these variables to your own name, age, etc.


# ---------------------------
# STRING OPERATIONS
# ---------------------------

# Concatenating (joining) strings using the + operator
greeting = "Hello, " + name + "!"
print("\n" + greeting)

# 📝 Practice: Try creating a new greeting message using a different name or add extra words.


# ---------------------------
# BASIC MATH OPERATIONS
# ---------------------------

# Define two number variables
x = 10
y = 3

# Perform basic arithmetic operations
sum_result = x + y
difference = x - y
product = x * y
quotient = x / y
modulus = x % y

# Print results of the math operations
print("\nMath with x =", x, "and y =", y)
print("Sum:", sum_result)
print("Difference:", difference)
print("Product:", product)
print("Quotient:", quotient)
print("Remainder:", modulus)

# 📝 Practice:
# - Change the values of x and y and re-run the program.
# - Try using different operators like `//` (integer division) or `**` (exponentiation).


# ---------------------------
# TYPE CASTING (CONVERSIONS)
# ---------------------------

# Convert integer to string
age_str = str(age)

# Convert float to integer (decimal part is dropped)
height_int = int(height)

print("\nAge as string:", age_str)
print("Height as integer:", height_int)

# 📝 Practice:
# Try converting your own input (like a string number) to an integer using int("5").


# ---------------------------
# USER INPUT
# ---------------------------

# Get input from the user (input always returns a string)
user_color = input("\nWhat's your favorite color? ")

# Show the value the user typed
print("Your favorite color is:", user_color)

# 📝 Practice:
# Add another input prompt to ask for the user's favorite food or number.


# ---------------------------
# LISTS AND INDEXING
# ---------------------------

# Create a list (ordered collection of items)
fruits = ["apple", "banana", "cherry", "date"]

# Access items using indexes (0 = first item)
print("\nFirst fruit:", fruits[0])
print("Last fruit:", fruits[-1])  # Negative index counts from the end

# Change a value in the list
fruits[1] = "blueberry"  # Replace "banana" with "blueberry"

# Print the updated list
print("Updated fruits list:", fruits)

# 📝 Practice:
# - Add another fruit to the list like: fruits.append("kiwi")
# - Try printing the second and third items.


# ---------------------------
# LENGTH (len)
# ---------------------------

# Find the number of characters in a string
print("\nLength of your name:", len(name))

# Find the number of items in a list
print("Number of fruits:", len(fruits))

# 📝 Practice:
# Try using len() on your favorite color or on another list like: ["dog", "cat", "fish"]

