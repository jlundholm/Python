from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)

all_bids = {}

restart = True
while restart == True:
  name = input("What is your name?: ")
  bid = input("What is your bid?: $")

  all_bids[name] = int(bid)

  again = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
  if again == 'no':
    restart = False
  else:
    clear()

#calculate results and display winner
highest_bidder = ""
highest_bid = 0
for key in all_bids:
  if all_bids[key] > highest_bid:
    highest_bid = all_bids[key]
    highest_bidder = max(all_bids, key=all_bids.get)
    
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")