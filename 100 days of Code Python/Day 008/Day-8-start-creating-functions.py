# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet():
  print("Hello")
  print("How do you do?")
  print("Isn't the weather nice today?")

greet()

# Function that allows for input
def greet_with_name(name):
  print(f"Hello, {name}")
  print(f"How do you do {name}?")
  print(f"Isn't the weather nice today {name}?")

greet_with_name("Jared")

# Function with more that 1 input

def greet_with(name, location):
  print(f"Hello, {name}")
  print(f"What is it like in {location}?")

greet_with("Jared", "Evanston")
greet_with(location="Evanston", name="Jared")