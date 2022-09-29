# defined the function
def ticketPrice(no_adults,no_children):
    price = (no_adults * 19.99) + (no_children * 8.99) + 2.50
    return price

# call / use the function

TotalPrice = ticketPrice(10,5)
print(TotalPrice)