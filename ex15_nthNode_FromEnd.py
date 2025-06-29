import LinkedList_Creation

def find_nthNode_FromEnd(head):
    n = int(input("Enter the position from the end: "))
    if n <= 0:
        print("Invalid")
        return
    else:
        first_pointer = head
        second_pointer = head

        for i in range(n):                                              # Moving first_pointer n steps forward
            if first_pointer is None:
                print("-1 (N is larger than the length of the list)")
                return
            first_pointer = first_pointer.next

        while first_pointer:                                            # Moving both the pointers until first_pointer reach the end
            first_pointer = first_pointer.next
            second_pointer = second_pointer.next

        print("The Nth node from the end is:", second_pointer.data)

head = LinkedList_Creation.create_Linked_List()
LinkedList_Creation.print_linked_list(head)
find_nthNode_FromEnd(head)
