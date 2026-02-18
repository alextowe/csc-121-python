# 5-3. Alien Colors #1
print("5-3. Alien Colors #1")

# passes 
alien_color = 'green'

print("\tThis test passes because the alien is green:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")

# fails
alien_color = 'yellow'

print("\n\tThis test fails because the alien is not green:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")

# 5-4. Alien Colors #2
print("\n5-4. Alien Colors #2")

# passes
alien_color = 'green'

print("\tThis if-else test passes because the alien is green:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")
else:
    print("\tYou just earned 10 points.")

# fails
alien_color = 'yellow'

print("\tThis if-else test fails because the alien is not green:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")
else:
    print("\tYou just earned 10 points.")

# 5-5. Alien Colors #3
print("\n5-5. Alien Colors #3")

# elif test passes for green
alien_color = 'green'

print("\tThis elif test passes because the alien is green:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")
elif alien_color == 'yellow':
    print("\tYou just earned 10 points.")
else:
    print("\tYou just earned 15 points.")

# elif test passes for yellow
alien_color = 'yellow'

print("\n\tThis elif test passes because the alien is yellow:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")
elif alien_color == 'yellow':
    print("\tYou just earned 10 points.")
else:
    print("\tYou just earned 15 points.")

# elif test passes for red
alien_color = 'red'

print("\n\tThis elif test passes because the alien is not green or yellow:")
if alien_color == 'green':
    print("\tYou just earned 5 points.")
elif alien_color == 'yellow':
    print("\tYou just earned 10 points.")
else:
    print("\tYou just earned 15 points.")