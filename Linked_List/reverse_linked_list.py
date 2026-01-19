#Reverse Linked List(leetcode)
#Reverse a linked list and return a new head

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next    #store next node
        curr.next = prev   #reverse pointer
        prev = curr        #move prev forward
        curr = nxt         #move curr forward

    return prev

def build_linked_list(values):
    dummy = ListNode(-1)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res =[]
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    head = build_linked_list([1,2,3,4,5])
    reversed_head = reverse_list(head)
    print("Reversed:", linked_list_to_list(reversed_head)) #[5,4,3,2,1]
    


    

