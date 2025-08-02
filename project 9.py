data_of_bidders = {}
bidders_more = True

while bidders_more:
    name = input("What is the name of the person?\n")
    bid_amt = int(input("What is the BID amount?\n"))  # Convert to int for comparison
    data_of_bidders[name] = bid_amt

    more_bidders = input("Are more people willing to bid? Yes/No\n").lower()

    if more_bidders == "no":
        bidders_more = False

        # Find highest bidder
        highest_bidder = max(data_of_bidders, key=data_of_bidders.get)
        amt = data_of_bidders[highest_bidder]
        print(f"\n💰 {highest_bidder} has the highest bid of ₹{amt}.")
    else:
        print("\n" * 100)  # Clears the screen (basic effect)
