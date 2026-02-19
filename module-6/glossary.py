words = {
    'variable': 'A storage location identified by a name that is connected to a value.',
    'list': 'A collection of items that can be of different types.',
    'tuple': 'An ordered, unchangeable collection of items.',
    'loop': 'Code that repeats as long as a specified condition is true.',
    'dictionary': 'A collection of key-value pairs that are unordered, changeable, and indexed.'
    }

for word, definition in words.items():
    print(f"{word.title()}:")
    print(f"\t{definition}\n")
