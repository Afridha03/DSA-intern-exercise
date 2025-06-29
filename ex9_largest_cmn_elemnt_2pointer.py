#input for the first array
num1 = int(input("Enter number of elements in first array: "))
arr1 = []
print("Enter elements for first array:")
for index in range(num1):
    num = int(input())
    arr1.append(num)

# input for the second array
num2 = int(input("Enter number of elements in second array: "))
arr2 = []
print("Enter elements for second array:")
for index in range(num2):
    num = int(input())
    arr2.append(num)

# Sort both arrays
arr1.sort()
arr2.sort()

pointer1 = len(arr1) - 1
pointer2 = len(arr2) - 1
found = False


while pointer1 >= 0 and pointer2 >= 0:
    if arr1[pointer1] == arr2[pointer2]:
        print("Largest common element is:", arr1[pointer1])
        found = True
        break
    elif arr1[pointer1] > arr2[pointer2]:
        pointer1 = pointer1 - 1
    else:
        pointer2 = pointer2 - 1

if found == False:
    print("No common element found.")
