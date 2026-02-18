numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for number in numbers:
    if number == 1:
        ordinal = '1st'
    elif number == 2:
        ordinal = '2nd'
    elif number == 3:
        ordinal = '3rd'
    else:
        ordinal = f"{number}th"
    
    print(ordinal)