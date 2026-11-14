#functions1: calculate total price of items
def calculate_subtotal(prices):
    return sum(prices)

#function2:calculate tax
def calculate_tax(subtotal,tax_rate):
    return subtotal*tax_rate/100

#function3: calculate final bill
def calculate_total(subtotal,tax):
    return subtotal+tax

# main program
prices=[100,200,150,50]
tax_rate=18
subtotal=calculate_subtotal(prices)
tax=calculate_tax(subtotal,tax_rate)
total=calculate_total(subtotal,tax)
print("subtotal",subtotal)
print("tax:",tax)
print("final bill",total)
