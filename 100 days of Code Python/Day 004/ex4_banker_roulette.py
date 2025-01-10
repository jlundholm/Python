import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
length = len(friends)
random_int = random.randint(0, length-1)
print(friends[random_int])

# can also use random.choice
# print (random.choice(friends))
