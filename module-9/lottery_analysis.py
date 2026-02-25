from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

def get_random_ticket(list):
    numbers = []
    while len(numbers) < 4:
        numbers.append(choice(list[:10]))
    numbers.append(choice(list[10:]))
    return numbers

winning_ticket = get_random_ticket(list)
counter = 0

while True:
    counter += 1
    my_ticket = get_random_ticket(list)

    if my_ticket == winning_ticket:
        print("Congratulations! You won the lottery!")
        break

print(f"It took {counter} tries to win the lottery.")