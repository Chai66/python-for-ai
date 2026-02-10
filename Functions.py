# Functions

# Functions are reusable blocks of code that do specific tasks. 
# Instead of writing the same code multiple times, 
# you write it once as a function and call it whenever needed.
def greet():
    print("Hello!!")
    print("Hello Again!!")

greet()

def say_goodbye():
    print("Goodbye!")
    print("See you later!")

# Call it multiple times
say_goodbye()
say_goodbye()
say_goodbye()

def check_weather():
    temperature = 25
    if temperature > 30:
        print("It's hot!")
    else:
        print("Nice weather!")

# Use the function
check_weather()

##Ex : Parameters
def greet(name):
    print(f"Hello, {name}")

greet(name="Shloka")
 
greet(name="Adam")

def introduce(name, age):
    print(f"My name is {name}")
    print(f"I am {age} years old")

# Call with values
introduce("Alice", 25)
introduce("Bob", 30)

def calculate_total(price, tax_rate, discount):
    tax = price * tax_rate
    final_price = price + tax - discount
    print(f"Total: ${final_price}")

# Order matters!
calculate_total(100, 0.08, 10)  # $98

# Return Values
#Getting results from functions

def add_print(a, b):
    print(a + b)

add_print(a=5, b=10)

def add_return(a, b):
    return a + b

add_print(a=5, b=10)

result = add_print(a=5, b=10)

result1 = result + 10

# Ex: 
def calculate_area(width, height):
    area = width * height
    return area

# Store the returned value
room_area = calculate_area(10, 12)
print(f"Room size: {room_area} sq ft")  # Room size: 120 sq ft

# Ex :
def double(number):
    return number * 2

# Store in variable
result = double(5)

# Use in expressions
total = double(5) + double(3)  # 10 + 6 = 16

# Pass to other functions
print(double(10))  # 20

# Use in conditions
if double(7) > 10:
    print("Big number!")

# RETURNING MULTIPLE VALUES
def get_min_max(numbers):
    return min(numbers), max(numbers)

# Get both values
minimum, maximum = get_min_max([5, 2, 8, 1, 9])
print(f"Min: {minimum}, Max: {maximum}")  # Min: 1, Max: 9

# Or as a tuple
result = get_min_max([5, 2, 8, 1, 9])
print(result)  # (1, 9)

# Return vs print

def get_greeting_print(name):
    print(f"Hello, {name}!")  # Just displays

def get_greeting_return(name):
    return f"Hello, {name}!"  # Gives back value

# Can't use print version's output
message = get_greeting_print("Alice")  # Prints but returns None
print(message)  # None

# Can use return version's output
message = get_greeting_return("Alice")  # Returns the string
print(message.upper())  # HELLO, ALICE!

# EXTERNAL TOOLS


# Understanding the terminology
# Let’s clarify what these terms mean:
# Module: A single Python file (like math.py)
# Package: A folder containing multiple modules
# Function: A reusable block of code (like print() or sqrt())
# Class: A blueprint for creating objects (we’ll cover this later)


# Pattern 1: Import the whole module
import math
# Now use: math.sqrt(16)

# Pattern 2: Import specific items from a module
from math import sqrt, pi
sqrt(16)

# Import entire module
import random

# Use module functions
number = random.randint(1, 10)
choice = random.choice(["apple", "banana", "orange"])

# Date and time
import datetime
today = datetime.date.today()
print(today)  # 2024-01-15

# Operating system
import os
current_dir = os.getcwd()
print(current_dir)

# JSON data
import json
data = {"name": "Alice", "age": 30}
json_string = json.dumps(data)



 