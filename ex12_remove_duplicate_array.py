num = int(input("Enter number of elements: "))
arr = []
print("Enter the elements :")
for elem in range(num):
    arr.append(int(input()))


if num == 0:
    print("Empty array.")
else:
    unique = [arr[0]]  
    for elem in range(1, num):
        if arr[elem] != arr[elem - 1]:  
            unique.append(arr[elem])

    print("Array after removing duplicates:")
    print(unique)
