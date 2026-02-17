# orginal guest list
guests = ['marcus aurelius', 'socrates', 'plato', 'aristotle']

name = guests[0].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[1].title()
print(f"Hello, {name}! You are invited to dinner.") 

name = guests[2].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[3].title()
print(f"Hello, {name}! You are invited to dinner.")

# Plato can't make it to dinner so he gets replaced with Diogenes
name = guests[2].title()
print(f"\n{name} can't make it to dinner.")
guests[2] = 'diogenes'

# new invitations
name = guests[0].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[1].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[2].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[3].title()
print(f"Hello, {name}! You are invited to dinner.")

# we have a bigger table so we can add more guests to the list
print("\nGood news! We found a bigger dinner table, so we can invite more guests!")
guests.insert(0, 'confucius')
guests.insert(2, 'epictetus')
guests.append('seneca')

# sort the list alphabetically
guests.sort()

# new invitations
name = guests[0].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[1].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[2].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[3].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[4].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[5].title()
print(f"Hello, {name}! You are invited to dinner.")

name = guests[6].title()
print(f"Hello, {name}! You are invited to dinner.")


# print the first three guests
print("\nThe first three items on the list are:")
for guest in guests[:3]:
    print(guest.title())


# print three guests from the middle of the list
print("\nThree items from the middle of the list are:")
middle_index = len(guests) // 2
for guest in guests[middle_index - 1:middle_index + 2]:
    print(guest.title())

# print the last three guests
print("\nThe last three items on the list are:")
for guest in guests[-3:]:
    print(guest.title())