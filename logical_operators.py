prices = [20, 25, 30, 18, 15]
decisions = []
for price in prices:
    if price > 20 and price < 30:
        decisions.append("Sell")
    elif price < 20 or price == 30:
        decisions.append("Buy")
    else:
        decisions.append("Hold")
print(decisions)