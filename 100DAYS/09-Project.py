#Creating a sale in where u can bid money for products


#ask for an Bid Price

bidders = {}
def addThem():
    nameUser = input("What's Your Name: ")
    bidPrice = int(input("How Much u gonna bid?:  "))
    bidders[nameUser] = bidPrice
def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Angela": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")

addThem()

while True:
    oneMore = input("There are poeple that wants bid more?: ")
    if oneMore.lower() == "yes":
        addThem()
    else:
        find_highest_bidder(bidders)
        break

print(bidders)


