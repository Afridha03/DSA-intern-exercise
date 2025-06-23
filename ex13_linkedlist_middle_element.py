class Node:                                             #class is created
    def __init__(self, data):                           #constructor with 2 attributes
        self.data = data
        self.next = None

node_count = int(input("Enter the number of nodes: "))   #get total node code from the user
num = int(input("Enter node1: "))                        #get first node from user
head = Node(num)                                         #created the first node as head
current = head

for index in range(2, node_count + 1):                       #used loop to add remaining nodes
    next_num = int(input("Enter node" + str(index) + ": "))
    new_node = Node(next_num)
    current.next = new_node                              #linked each node
    current = new_node

print("\nOriginal Linked List:")
current = head                                           # Reset current to head
while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")

slow_pointer = head                         
fast_pointer = head                                      #2 pointers are created
while fast_pointer and fast_pointer.next:
    slow_pointer = slow_pointer.next
    fast_pointer = fast_pointer.next.next                 #checking the middle element using loop


print("\nMiddle element is:", slow_pointer.data)
