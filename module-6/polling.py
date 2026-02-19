favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

people = ['jen', 'sarah', 'edward', 'phil', 'alex', 'maria', 'john']

for person in people:
    if person in favorite_languages.keys():
        print(f"Thank you, {person.title()}, for taking the poll.")
    else:
        print(f"{person.title()}, please take our poll.")