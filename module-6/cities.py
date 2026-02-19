cities = {
    'dublin': {
        'country': 'ireland',
        'population': 1570000,
        'fact': 'Dublin was founded by Vikings in the 9th century, is the capital and largest city of Ireland'
        },
    'london': {
        'country': 'united kingdom',
        'population': 9820000,
        'fact': 'London is the capital and largest city of England and the United Kingdom.'
        },
    'tokyo': {
        'country': 'japan',
        'population': 33400000,
        'fact': "Tokyo is the capital and largest city of Japan."
        }
    }

for city, info in cities.items():
    print(f"\n{city.title()} is in {info['country'].title()}.")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")