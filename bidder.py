from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
def add_dict(bname, bamount):
  bid_dict["Name"] = bname
  bid_dict["Bid Amount"]= bamount




bidder = True
bid_dict={}
while bidder:
  name = input("Enter your name ")
  bid = int(input("Enter your bid Amount"))
  bid_dict[name] =bid
  ppl =input("Any more bidder yes or no: ").lower()
  if ppl == "no":
    bidder= False
  else:
    clear()

print(bid_dict)
hno=0
name = ''
for bid in bid_dict:
  if int(bid_dict[bid]) > hno:
    hno =int(bid_dict[bid])
    name = bid
print(f'Winner is {name} and bid amount is {hno}')


  



