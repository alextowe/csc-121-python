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
print(f"{name} can't make it to dinner.")

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