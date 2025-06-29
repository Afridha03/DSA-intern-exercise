class Node:
    def __init__(self, name, roll, tamil, english, maths):
        self.name = name
        self.roll = roll
        self.tamil = tamil
        self.english = english
        self.maths = maths
        self.total = tamil + english + maths
        self.average = self.total / 3
        self.next = None

def insert_info(head, name, roll, tamil, english, maths):
    new_node = Node(name, roll, tamil, english, maths)
    if head is None:
        return new_node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = new_node
        return head

def display_info(head):
    current = head
    print("\n--- Student Records ---")
    while current:
        print(f"\nName: {current.name}")
        print(f"Roll Number: {current.roll}")
        print(f"Tamil: {current.tamil}")
        print(f"English: {current.english}")
        print(f"Maths: {current.maths}")
        print(f"Total: {current.total}")
        print(f"Average: {current.average:.2f}")
        current = current.next
head = None
ask = "yes"
while ask.lower() == "yes":
    name = input("NAME : ")
    roll = int(input("ROLL NUMBER : "))
    print("ENTER YOUR GRADES (OUT OF 100)")
    tamil = int(input("TAMIL : "))
    english = int(input("ENGLISH : "))
    maths = int(input("MATHS : "))

    head = insert_info(head, name, roll, tamil, english, maths)

    print(f"TOTAL (OUT OF 300): {tamil + english + maths}")
    print(f"AVERAGE: {(tamil + english + maths)/3:.2f}")

    ask = input("Do you want to add another student? (yes/no): ")

display_info(head)
