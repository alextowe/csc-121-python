sandwich_orders = ['turkey', 'ham and cheese', 'tuna', 'chicken', 'veggie']
finished_sandwiches = []

print("Sandwiches being made:")
while sandwich_orders:
    current_sandwich = sandwich_orders.pop(0)
    print(f"\tMaking your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)
    
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"\tThe {sandwich} sandwich is ready.")