import LinkedList_Creation

def linked_list_reverse(head):
    prev = None
    current = head
    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

head = LinkedList_Creation.create_Linked_List()
LinkedList_Creation.print_linked_list(head)
reversed_head = linked_list_reverse(head)
print("\nReversed Linked List:")
LinkedList_Creation.print_linked_list(reversed_head)
