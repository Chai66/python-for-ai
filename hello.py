first_name = "chaitanya"
last_name = "chalumuri"
full_name = first_name + " "+ last_name
long_dash = "_" * 15
print(full_name)
print(long_dash)

message = "I love Python programming with Python"

# Check if something exists
print("Python" in message)        # True
print(message.startswith("I"))   # True
print(message.endswith("Python")) # True

# Find position
print(message.find("Python"))     # 7 (first occurrence)
print(message.count("Python"))    # 2 (number of times)

# Replace
new_message = message.replace("Python", "JavaScript")
print(new_message)  # "I love JavaScript programming with JavaScript"

temperature = 25

if temperature >25:
    print("It's hot!")
else:
    print("It's nice weather!")

    score = 50

if score >= 90:
    print("A - Excellent!")
elif score >= 80:
    print("B - Good job!")
elif score >= 70:
    print("C - Keep it up!")
else:
    print("F - Need improvement")

    ## Loop
for i in range(5):
    print("Shloka")

# Count from 1 to 5
for i in range(1, 6):
    print(i)
# Output: 1, 2, 3, 4, 5

# Count by 2s
for i in range(0, 10, 2):
    print(i)
# Output: 0, 2, 4, 6, 8

#### DATA STRUCTURES ##########

# Empty list
my_list = []

# List with items
fruits = ["apple", "banana", "orange"]
numbers = [1, 2, 3, 4, 5]
mixed = ["hello", 42, True, 3.14]  # Different types OK!

age = 25
has_license = False

my_list = ["Shloka",4,age,has_license]

name = my_list[0]
age = my_list[1]

fruits = ["apple", "banana", "orange"]

# Change an item
fruits[0] = "mango"
print(fruits)  # ["mango", "banana", "orange"]

# Add items
fruits.append("grape")      # Add to end
fruits.insert(1, "kiwi")    # Insert at position

# Remove items
fruits.remove("banana")     # Remove by value
last = fruits.pop()        # Remove and return last
del fruits[0]              # Remove by index


## What are dictionaries?
##Dictionaries store data in key-value pairs. Think of them like a 
# real dictionary where you look up a word (key) to find its definition 
# 
my_dict = {}

# Dictionary with data
person = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

person["age"]

# Different ways to create
scores = dict(math=95, english=87, science=92)(value).

person = {"name": "Alice", "age": 30, "city": "New York"}

# Get all keys, values, or items
print(person.keys())    # dict_keys(['name', 'age', 'city'])
print(person.values())  # dict_values(['Alice', 30, 'New York'])
print(person.items())   # dict_items([('name', 'Alice'), ...])

# Check if key exists
if "name" in person:
    print("Name found!")

# Update multiple values
person.update({"age": 31, "job": "Engineer"})


##
# What are tuples?
# Tuples are like lists, but they can’t be changed once created. They’re immutable (unchangeable) sequences.
# Use tuples for data that shouldn’t change:
# Coordinates (x, y)
# RGB colors (255, 0, 0)
# Database records
# Function return values

# Empty tuple
empty = ()

# Tuple with items
point = (3, 5)
colors = ("red", "green", "blue")

# Single item tuple needs comma!
single = (42,)  # Note the comma
not_tuple = (42)  # This is just 42 in parentheses

# Without parentheses (implicit)
coordinates = 10, 20


# What are sets?
# Sets are collections that only store unique values. They automatically remove duplicates.
# Think of sets like:
# A bag of unique marbles
# Guest list (each person once)
# Unique tags or categories

# Empty set (careful!)
empty_set = set()  # NOT {} - that's a dict!

# Set with values - both ways work
numbers = {1, 2, 3, 4, 5}
fruits = set(["apple", "banana", "orange"])

# From a list (removes duplicates)
scores = [85, 90, 85, 92, 90]
unique_scores = set(scores)  # {85, 90, 92}