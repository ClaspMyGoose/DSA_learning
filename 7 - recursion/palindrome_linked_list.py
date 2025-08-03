class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def isPalindrome(head: ListNode) -> bool:


# ! this shit is beyond fucked up and not working lol 

    if not head:
        return False 
    # have head, need to get tail 

    lookaheadTail = head

    # stop 1 before end safely 
    while lookaheadTail.next and lookaheadTail.next.next: 
        lookaheadTail = lookaheadTail.next 

    # have head and tail (lookaheadTail.next) 

    if head.val == lookaheadTail.next.val: 
        lookaheadTail.next = None 
        check = isPalindrome(head.next)
    else: 
        return False 

    return (True and check)

case1 = [1,2,2,1]
case4 = [1,2,3,4]
case5 = [1,2,4,2,2]
case6 = [1,2,3,2,1]
    # [1,2,2,1]
arr = [] # passes 
arr = [1]


dummyHead = ListNode(None, None)
prevNode = dummyHead 

for i in range(len(arr)):
    node = ListNode(arr[i])     
    prevNode.next = node 
    prevNode = node 

isPalindrome(dummyHead.next)