def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0)) # you cannot divide by 0 so program crashes, you don't want this to happen in a live program
print(spam(1))