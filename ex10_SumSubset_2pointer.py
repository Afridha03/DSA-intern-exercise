# Getting input from the user
n = int(input("Enter number of elements: "))
if n < 0:
    print("Invalid number")
else:
    arr = []
    print("Enter the elements:")
    for i in range(n):
        arr.append(int(input()))

    target = int(input("Enter the target sum: "))
    
    if target < 0:
        print("Invalid target number")
    else:
        arr.sort()
        i = 0
        j = len(arr) - 1
        pairs = []

        while i < j:
            current_sum = arr[i] + arr[j]
            if current_sum == target:
                pairs.append(f"{arr[i]},{arr[j]}")
                i = i + 1
                j = j - 1
            elif current_sum < target:
                i = i + 1
            else:
                j = j - 1

        if len(pairs) == 0:
            print("No pair found.")
        else:
            print(" and ".join(pairs))
