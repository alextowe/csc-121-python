pizzas = ['pepperoni', 'cheese', 'hawaiian']
friend_pizzas = pizzas[:]

pizzas.append('vegetarian')
friend_pizzas.append('meat lovers')

print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)