favorite_places = {
    'alex': ['dublin', 'london', 'tokyo'],
    'noah': ['new york', 'sydney', 'rome'],
    'bryson': ['berlin', 'amsterdam', 'barcelona']
    }

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"\t{place.title()}")