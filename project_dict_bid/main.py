bids = {}
bidding_finishes = False
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of Rs. {highest_bid}")
while not bidding_finishes:
    name = input("What is your name :")
    bid = int(input("What is your bid Rs.: "))
    bids[name] = bid
    should_continue = input("Are there any other bidders ? Type 'yes' or 'no' :")
    if should_continue == "no":
        bidding_finishes = True
        find_highest_bidder(bids)
