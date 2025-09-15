#account → variable name (like a box we’re labeling).
# = → assignment (put something inside the box).

account = {                          # {} → means we’re creating a dictionary.
    "trader": "Yash",                # "trader" = the key. Keys are always in quotes because 
                                     # they’re treated like labels(strings), not variables.
                                     # : → means “maps to.”
                                     # "Yash" = the value.
    "balance": 10000,
    "profit": 350.75,
    "active": True
}

# Updating the dictionary
account["balance"] = 12000   # update balance
account["profit"] = 200.67   # update profit

print(account["trader"])   # Yash
print(account["balance"])  # 12000
print(account["profit"])   # 200.67
print(account["active"])   # True
#So "trader": "Yash" means → the dictionary has a key called "trader", and its value is "Yash".

# Number of trades taken. Created a dictionary for each trade.

trade_1 = {
    "stock": "AAPL",
    "entry": 400,
    "exit": 450,
    "pnl": 450 - 400
}

trade_2 = {
    "stock": "GOOG",
    "entry": 350,
    "exit": 600,
    "pnl": 600 - 350
}

portfolio = [trade_1, trade_2] #Created a list called portfolio.

total_pnl = 0   # created this variable to get total of pnl of all trades.
for trade in portfolio:     #for every trade in portfolio one by one.
    total_pnl += trade["pnl"]   # total_pnl = total_pnl + trade["pnl"] can use this as well.

    #Step-by-step version:
    #Start with total_pnl = 0 (begin with nothing).
    #First round of loop:
    # trade = first dictionary
    #total_pnl = 0 + trade["pnl"]
    #Second round of loop:
    #trade = second dictionary
    #total_pnl = (previous total) + trade["pnl"]
    #And so on… until all trades are added.
print(f"Total pnl is {total_pnl}.")