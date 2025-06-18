set_one = []
set_two = []

print("Enter 5 elements for first set:")
for num in range(1, 6):
    element = int(input("Enter element " + str(num) + ": "))
    set_one.append(element)

print("Enter 5 elements for second set:")
for num in range(1, 6):
    element = int(input("Enter element " + str(num) + ": "))
    set_two.append(element)

intersection= []

for element in set_one:
    if element in set_two and element not in intersection:
        intersection.append(element)

print("Intersection of the two sets is:", intersection)
