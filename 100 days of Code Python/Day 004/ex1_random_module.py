import random

random_integer = random.randint(1, 10)
print(random_integer)

# includes zero, but not 1
random_number_0_to_1 = random.random()
print(random_number_0_to_1)

# can include zero and 1
random_float = random.uniform(1, 10)
print(random_float)
