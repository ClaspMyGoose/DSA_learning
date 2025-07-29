class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def reverseList(head):
        
    prev = None 
    
    # given the head 
    # ! key insight, I have to process each Node, not just traverse the list 
    # can't check head.next, have to check head 
    # (which at the end would be None, the value of the last node next ptr)
    # once I've processed the last node and set head = head.next = None 
    # I've traversed AND PROCESSED the list and prev is my new head 
    while head is not None: 
        nextNode = head.next
        head.next = prev  
        prev = head 
        head = nextNode 
            

    # 1 , 2 , 3 , 4 , 5 

    return prev 




prev = None
for i in range(5):
    node = ListNode(5 - i, prev)
    prev = node 

reverseList(node)