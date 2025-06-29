class Node:
    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.next = None

def insert_at_first(head, name, location):
    new_node = Node(name, location)
    new_node.next = head
    return new_node

def insert_at_last(head, name, location):
    new_node = Node(name, location)
    if head is None:
        return new_node
    current = head
    while current.next:
        current = current.next
    current.next = new_node
    return head

def insert_at_position(head, name, location, position):
    new_node = Node(name, location)
    if position <= 1 or head is None:
        return insert_at_first(head, name, location)
    current = head
    count = 1
    while current.next and count < position - 1:
        current = current.next
        count += 1
    new_node.next = current.next
    current.next = new_node
    return head

def reverse_list(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

def display_list(head):
    print("\n--- Linked List ---")
    if head is None:
        print("List is empty.")
        return
    current = head
    while current:
        print(f"Name: {current.name}, Location: {current.location}")
        current = current.next

# Main program
head = None
while True:
    print("\nChoose an option:")
    print("1. Insert at first")
    print("2. Insert at last")
    print("3. Insert at position")
    print("4. Reverse the list")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice in ["1", "2", "3"]:
        while True:
            name = input("Enter Name: ")
            location = input("Enter Location: ")

            if choice == "1":
                head = insert_at_first(head, name, location)
            elif choice == "2":
                head = insert_at_last(head, name, location)
            elif choice == "3":
                pos = int(input("Enter position to insert at: "))
                head = insert_at_position(head, name, location, pos)

            ask = input("Do you want to add another? (yes/no): ").lower()
            if ask != "yes":
                break

        display_list(head)  # ✅ NOW ADDED BACK

    elif choice == "4":
        head = reverse_list(head)
        print("Linked list reversed.")
        display_list(head)

    elif choice == "5":
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please choose between 1-5.")
