# [] = lists (ordered, changable)
# A list of stock prices
prices = [100.5, 101.2, 102.8, 99.7]  #Square brackets [] → used for lists (ordered collection of 
                                      #items).

print(prices)
print(prices[0])   # first item
print(prices[-1])  # last item

prices.append(105.3)   # ".append" add new price at the end
print(prices)

prices[1] = 101.5  # updating the value of an item of the list
print(prices)

print(len(prices))  # "len" adds the number of items available in the list which in this case is 5