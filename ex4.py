arr_num = []
for num in range(1, 5):
    integer = int(input("enter num" + str(num) + ":"))
    arr_num.append(integer)
print("array is", arr_num)

target_num = int(input("enter your target num:"))
found = False
for num1 in range(len(arr_num)):
    for num2 in range(num1 + 1, len(arr_num)):
        if arr_num[num1] + arr_num[num2] == target_num:
            print("Output: index", num1, "and", num2)
            found = True
            break
    if found:
        break
if not found:
    print("No pair adds up to the target.")
