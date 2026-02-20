sandwich_order = ['pastrami', 'turkey', 'ham and cheese', 'pastrami', 'tuna', 'pastrami', 'chicken', 'veggie']

print("The deli has run out of pastrami.")
while 'pastrami' in sandwich_order:
    sandwich_order.remove('pastrami')