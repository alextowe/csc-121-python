favorite_numbers = {
    'alex': [1, 2, 3],
    'noah': [7, 13, 21],
    'troy': [3, 9, 27],
    'cody': [4, 8, 16],
    'bryson': [9, 18, 27]
    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"\t{number}")