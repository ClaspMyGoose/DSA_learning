class ListNode: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        
        if not head:
            return head 

        cur = head 

        if cur.next:
           new_head = self.reverseList(cur.next) 
        
        else:
            return cur  

        cur.next.next = cur 
        cur.next = None 

        return new_head 
     



# a = ListNode('A')
# b = ListNode('B')
# a.next = b 
# c = ListNode('C')
# b.next = c 

# sol = Solution() 

# sol.reverseList(a)
