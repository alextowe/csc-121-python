languages = ['english', 'spanish', 'french', 'german']
print(languages)

# adding items to a list
languages.append('italian')
languages.insert(0, 'japanese')
print(languages)

# removing items from a list
del languages[3]
languages.remove('german')
popped_language = languages.pop(1)
print(f"The first language I learned was {popped_language.title()}.")
print(languages)

languages = ['english', 'spanish', 'french', 'german']
print(languages)

print(sorted(languages))
languages.reverse()
print(languages)
