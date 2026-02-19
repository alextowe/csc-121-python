pets = []

pet = {
    'name': 'ivy',
    'owner': 'alex',
    'species': 'cat',
    'age': 3,
    'color': 'black'
    }
pets.append(pet)

pet = {
    'name': 'dex',
    'owner': 'bryson',
    'species': 'dog',
    'age': 12,
    'color': 'white'
    }
pets.append(pet)

pet = {
    'name': 'lemon',
    'owner': 'alex',
    'species': 'snake',
    'age': 5,
    'color': 'yellow'
    }
pets.append(pet)

for pet in pets:
    print(f"{pet['name'].title()} is a {pet['age']} year old {pet['color']} {pet['species']} owned by {pet['owner'].title()}.")