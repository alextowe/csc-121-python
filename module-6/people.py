people = []

person = {
    'first_name': 'noah',
    'last_name': 'person',
    'age': 28,
    'city': 'asheville'  
    }
people.append(person)

person = {
    'first_name': 'sarah',
    'last_name': 'person',
    'age': 25,
    'city': 'charlotte'
    }
people.append(person)

person = {
    'first_name': 'jeffrey',    
    'last_name': 'person',
    'age': 30,
    'city': 'raleigh'
    }
people.append(person)

for person in people:
    print(f"{person['first_name'].title()} {person['last_name'].title()} is {person['age']} years old and lives in {person['city'].title()}.")