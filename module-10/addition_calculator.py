print("Give me two numbers, and I will add them together.")
print("Enter 'q' to quit.\n")

while True:
    first_number = input("First number: ")
    if first_number.lower() == 'q':
        break
    second_number = input("Second number: ")
    if second_number.lower() == 'q':
        break

    try:
        answer = int(first_number) + int(second_number)
    except ValueError:
        print("Please enter valid numbers.\n")
    else:
        print(f"The sum of {first_number} and {second_number} is {answer}.\n")
