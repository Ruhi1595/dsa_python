#Merge Two sorted lists(leetcode)
#Merge Two sorted linked lists and return the merged sorted lists

class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next

def merge_two_lists(list1, list2):
    #Dummy node helps us build the merged list easily
    dummy = ListNode(-1)
    current = dummy

    #Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next

        else:
            current.next = list2
            list2 = list2.next
        
        current = current.next
    
    #Attach the remaining nodes(only one list will have nodes left)
    if list1:
        current.next = list1
    else:
        current.next = list2

    return dummy.next

#Helper function : Convert python list --> linked list
def build_linked_list(values):
    dummy = ListNode(-1)
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

#Helper function : Convert linked list --> python list(for printing)
def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    # Example test
    l1 = build_linked_list([1, 2, 4])
    l2 = build_linked_list([1, 3, 4])

    merged = merge_two_lists(l1, l2)
    print("Merged List:", linked_list_to_list(merged))  # [1, 1, 2, 3, 4, 4]


    

