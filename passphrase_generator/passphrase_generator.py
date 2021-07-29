import random
import wordlist

#variables
nr_password = []
r_password = ""

#program start
print("Welcome to the phasephrase generator!")
nr_input = int(input("How many words would you like in your phasephrase?\n"))
nr_password.extend(random.sample(wordlist.words, nr_input))

#print(nr_password)
random.shuffle(nr_password)
print("\n")
print(nr_password)
for char in nr_password:
    r_password += char

print(f"\nYour passphrase is: {r_password}")

