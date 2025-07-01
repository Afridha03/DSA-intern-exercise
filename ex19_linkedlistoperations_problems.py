#a class has been created called "Node"
class Node:
    #constructor with attributes - name, location
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.next = None

        
#this method is used for inserting the node at the end of the linked list by passing the parameters
#the parameters - name, location
def insert_at_end(head, name, location):
    new_node = Node(name, location)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head



#this method is used for inserting the node at the beginning of the linked list by passing the parameters
#the parameters - name, location
def insert_at_first(head, name, location):
    new_node = Node(name, location)
    new_node.next = head
    return new_node



#this method is used for inserting the node at a specific position in a linked list
#the parameters - name, location, position 
def insert_at_position(head, name, location, position):
    new_node = Node(name, location)
    if position <= 1:
        print("invalid")
    current = head
    count = 1
    while current.next and count < position - 1:
        current = current.next
        count = count + 1
    new_node.next = current.next
    current.next = new_node
    return head




#this method is used for deleting a node in a linked list by  passing the node value
#input parameter - target_name
def delete_by_name(head, target_name):
    if head.name == target_name:
        return head.next
    current = head
    while current.next and current.next.name != target_name:
        current = current.next
    if current.next:
        current.next = current.next.next
    else:
        print("Name not found.")
    return head




#this method is used for reversing the linked list by passing the node value
def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev



#this method will display the linked list
def display_list(head):
    print("\n--- Linked List ---")
    if head is None:
        print("List is empty.")
    else:
        current = head
        count = 1
        while current:
            print(f"Node {count}: {current.name}, {current.location}")
            current = current.next
            count = count + 1



head = None
print("CREATE YOUR LINKED LIST")


#this is the menu contains linked list operations
while True:
    print("\nChoose an option:")
    print("1. Add node at the end")
    print("2. Add node at the first")
    print("3. Add node at position")
    print("4. Delete a node by name")
    print("5. Display the linked list")
    print("6. Reverse the linked list")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ")

    

    #this pass the parameters to the "insert_at_end" method
    if choice == "1":
        ask = "yes"
        while ask == "yes":
            name = input("Enter Name: ")
            location = input("Enter Location: ")
            head = insert_at_end(head, name, location)
            ask = input("want to add another node? (yes/no): ")

            
            
            
    #this pass the parameters to the "insert_at_end" method
    elif choice == "2":
        ask = "yes"
        while ask == "yes":
            name = input("Enter Name: ")
            location = input("Enter Location: ")
            head = insert_at_first(head, name, location)
            ask = input("want to add another node? (yes/no): ")

            

            
    #this pass the parameters to the "insert_at_position" method
    elif choice == "3":
        ask = "yes"
        while ask == "yes":
            name = input("Enter Name: ")
            location = input("Enter Location: ")
            position = int(input("Enter position: "))
            head = insert_at_position(head, name, location, position)
            ask = input("want to add another node? (yes/no): ")

            


    #this pass the parameters to the "delete_by_name" method
    elif choice == "4":
        ask = "yes"
        while ask == "yes":
            name = input("Enter name to delete: ")
            head = delete_by_name(head, name)
            ask = input("want to delete another node? (yes/no): ")

            

            
    #this pass the parameters to the "display_list" method
    elif choice == "5":
        display_list(head)

        

        
    #this pass the parameters to the "reverse_list" method
    elif choice == "6":
        head = reverse_list(head)
        print("Linked list reversed.")
        display_list(head)

        


    #this will exit from the program
    elif choice == "7":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")
