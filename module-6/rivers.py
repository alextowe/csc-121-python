rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'yellow': 'china',
    'parana': 'argentina',
    }

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers:")
for river in rivers.keys():
    print(f"\t{river.title()}")

print("\nCountries:")
for country in rivers.values():
    print(f"\t{country.title()}")