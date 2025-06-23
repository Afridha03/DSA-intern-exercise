n = int(input("Enter number of elements: "))
arr = []
print("Enter the elements (in sorted order):")
for i in range(n):
    arr.append(int(input()))


if n == 0:
    print("Empty array.")
else:
    unique = [arr[0]]  
    for i in range(1, n):
        if arr[i] != arr[i - 1]:  
            unique.append(arr[i])

    print("Array after removing duplicates:")
    print(unique)
