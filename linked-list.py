# -------------------------Creating Linked List-------------------------#

# Creating Node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Printing Linkedlist items


def ll_print(ll):
    if(ll == None):
        print("Empty LL")
    while (ll):
        print(ll.val, end=" ")
        ll = ll.next
    print(" ")


# Creating ll:

def ll_create(arr):
    head = ListNode(0)
    temp = ListNode(0)
    temp.next = head

    for _ in arr:
        node = ListNode(_)
        head.next = node
        head = node
    return temp.next.next
