class Node:
    def __init__(self, loc, node):
        self.loc = loc
        self.node = node
        self.next = None
def insert_Location(head, loc):
    location = Node(loc)
    head = current
    for i in range(node - 1):
        current.next = location
        current = current.next
        return head
def display(head):
    current = head
    print(f"location : {current.location}")
    current = current.next
head = None
ask = "yes"
while ask.lower() == "yes":
    loc = input("Enter a Location :" )
    node = int(input("Enter a Node num :"))

    location = insert_Location(head, loc)
    ask = input("Do you want to add another location? (yes/no): ")

display(head)
