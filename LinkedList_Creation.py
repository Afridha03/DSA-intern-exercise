# LinkedList_creation
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def create_Linked_List():
    ask = "yes"
    head = None
    current = None
    while(ask =="yes"):
        if(ask == "yes"):
           num = int(input("Enter a Num : "))
           new_node = Node(num)
           if head is None:
               head = new_node
               current = new_node
           else:
               current.next = new_node
               current = new_node
        ask = input("do you want to add a node?(yes/no):")
    return head
           
def print_linked_list(head):
    print("\nOriginal Linked List:")
    current = head
    while current:
        print(current.data,end="->")
        current = current.next
    print("None")
