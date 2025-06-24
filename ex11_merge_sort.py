def merge(left, right):
    result = []
    i = 0
    j = 0

    # Compare and merge
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1

    
    while i < len(left):
        result.append(left[i])
        i = i + 1

    while j < len(right):
        result.append(right[j])
        j = j + 1

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)


n = int(input("Enter number of elements: ")) #size of the array
arr = []
print("Enter the elements:")
for i in range(n): 
    arr.append(int(input()))


sorted_arr = merge_sort(arr)


print("Sorted array:")
print(sorted_arr)
