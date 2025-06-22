#input for the first array
n1 = int(input("Enter number of elements in first array: "))
arr1 = []
print("Enter elements for first array:")
for index in range(n1):
    num = int(input())
    arr1.append(num)

# input for the second array
n2 = int(input("Enter number of elements in second array: "))
arr2 = []
print("Enter elements for second array:")
for index in range(n2):
    num = int(input())
    arr2.append(num)

# Sort both arrays
arr1.sort()
arr2.sort()

i = len(arr1) - 1
j = len(arr2) - 1
found = False


while i >= 0 and j >= 0:
    if arr1[i] == arr2[j]:
        print("Largest common element is:", arr1[i])
        found = True
        break
    elif arr1[i] > arr2[j]:
        i = i - 1
    else:
        j = j - 1

if found == False:
    print("No common element found.")
