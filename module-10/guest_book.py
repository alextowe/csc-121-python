from pathlib import Path

name_string = ''
while True:
    name = input("What is your name? (type 'q' to quit)\n")
    if name.lower() == 'q':
        break

    print(f"\nHello, {name.title()}! I'm adding your name to the guest book.\n")
    name_string += f"{name}\n"

path = Path('guest_book.txt')
path.write_text(name_string)