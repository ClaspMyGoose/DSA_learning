# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
    

        # was overcomplicating these at first 
        # if both are None, we can return either 
        # which simplifies to this which handles all three 
        # l1 = None l2 = None 
        # l1 = True l2 = None 
        # l1 = None l2 = True 
        if not list1:
            return list2
        if not list2:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2  
    

