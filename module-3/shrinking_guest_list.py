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

# we can only invite two guests to dinner
print("\nUnfortunately, our new dinner table won't arrive in time, so we can only invite two guests to dinner.")

# remove guests until only two remain
name = guests.pop()
print(f"Sorry, {name.title()}, we can't invite you to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()}, we can't invite you to dinner.") 

name = guests.pop()
print(f"Sorry, {name.title()}, we can't invite you to dinner.")

name = guests.pop()
print(f"Sorry, {name.title()}, we can't invite you to dinner.")
name = guests.pop()
print(f"Sorry, {name.title()}, we can't invite you to dinner.")

# invitations for the remaining guests
name = guests[0].title()
print(f"Hello, {name}! You are still invited to dinner.")

name = guests[1].title()
print(f"Hello, {name}! You are still invited to dinner.")

# for assignment 3-9. Dinner Guest 
print(f"\nI am inviting {len(guests)} guests to dinner.")

# remove the last two guests from the list
del guests[0]
del guests[0]
print(guests)
