import random
import wordlist

# variables
nr_password = []
r_password = ""
test = 32

# Input from user
print("Welcome to the phasephrase generator!")

while True:
    nr_input = input("How many words would you like in your phasephrase? Normally 4-6 words.\n")
    try:
        nr_input=int(nr_input)
    except:
        print("\nPlease use numeric digits.")
        continue
    if nr_input < 1:
        print("\nPlease enter a positive number.")
        continue
    break

#create a list from random words from wordlist
nr_password.extend(random.sample(wordlist.words, nr_input))

#print(nr_password)
random.shuffle(nr_password)
print("\n")
print(nr_password)
for char in nr_password:
    r_password += char

if nr_input > 6:
    print("\nYour passphrase is going to be very long and might be hard to remember.")

print(f"\nYour super random secret and secure passphrase is: {r_password}")


