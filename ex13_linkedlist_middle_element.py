#finding middle element in a linked list
import LinkedList_Creation

head = LinkedList_Creation.create_Linked_List()
LinkedList_Creation.print_linked_list(head)

def finding_middle_element(head):
    slow_pointer = head
    fast_pointer = head
    while fast_pointer and fast_pointer.next:
        slow_pointer = slow_pointer.next
        fast_pointer = fast_pointer.next.next
    print("Middle element is : " ,slow_pointer.data)
    
finding_middle_element(head)
