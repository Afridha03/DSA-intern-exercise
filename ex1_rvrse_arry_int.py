#reverse the array using consecutive k integer
arr=[]
for index in range(1,10):
    element = int(input("enter element no"+str(index)+":"))
    arr.append(element)
print(arr)
size = int(input("enter an integer: "))
index=0
while(index<len(arr)):
    end = index + size
    sub_array = arr[index:end]
    sub_array.reverse()
    arr[index:end] = sub_array
    index = index + size
print(arr)
