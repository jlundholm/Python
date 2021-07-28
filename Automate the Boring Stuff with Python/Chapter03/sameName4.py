def spam():
    print(eggs)
    eggs = 'spam local'

eggs = 'global'

spam() # local variable 'eggs' referenced before assignment