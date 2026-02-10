locations = ['london', 'tokyo', 'sydney', 'rome', 'dublin'] 
print(locations)

# list is sorted but not changed
print(sorted(locations))
print(locations)

# list is sorted in reverse but not changed
print(sorted(locations, reverse=True))
print(locations)

# list is reversed and changed
locations.reverse()
print(locations)

# list is reversed again and changed back to original order
locations.reverse()
print(locations)

# sort list in alphabetical order
locations.sort()
print(locations)

# sort list in reverse alphabetical order
locations.sort(reverse=True)
print(locations)