def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice?")

greet()


user_name = input("What is your name?")
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}")

greet_with_name(user_name)