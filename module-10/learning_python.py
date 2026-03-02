from pathlib import Path

path = Path('learning_python.txt')
contents = path.read_text().rstrip()

# read the entire file
print('Reading the entire file:')
print(contents)

# read the file line by line
print('\nReading the file line by line:')
for line in contents.splitlines():
    print(line)
