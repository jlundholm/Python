def spam():
    eggs = 99
    bacon()
    print(eggs)

def bacon():
    ham = 101
    eggs = 0

spam()
print(eggs) #the eggs variable doesn't exsist outside of the spam funtion, it's a local variable not a global