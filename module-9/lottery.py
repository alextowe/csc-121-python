from random import choice

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
winning_numbers = []

while len(winning_numbers) < 4:
    winning_numbers.append(choice(list[:10]))

winning_numbers.append(choice(list[10:]))

user_numbers = []
while len(user_numbers) < 4:
    user_numbers.append(int(input("Enter a number between 1 and 10: ")))

user_numbers.append(input("Enter a letter between A and E: "))

print("Winning numbers: ", winning_numbers)
print("Your numbers: ", user_numbers)

if user_numbers == winning_numbers:
    print("Congratulations! You're a winner!")
else:    
    print("Sorry, you lost")