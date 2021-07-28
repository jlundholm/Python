def spam():
    global eggs
    eggs = 'spam' # eggs has been made a global variable

def bacon():
    eggs = 'bacon' # unrelated local eggs variable

def ham():
    print(eggs) # it going to print the global eggs variable

eggs = 42 # global eggs variable

spam()

print(eggs)