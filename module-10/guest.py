from pathlib import Path

name = input("What is your name? ")
print(f"Hello, {name}! I'm writing your name to a file.")

path = Path('guest.txt')
path.write_text(name)