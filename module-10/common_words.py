from pathlib import Path

path = Path('beowulf.txt')

try:
    contents = path.read_text()
except FileNotFoundError:
    print(f"Sorry, the file {path} does not exist.")
else:
    words = contents.lower().count('the ')
    print(f"'The' appears {words} times in the file {path}.")