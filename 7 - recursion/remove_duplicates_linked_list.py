
class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next



#        x, y, z 
# arr = [1,1,2]

# 1
#  - perfectList is None 
#  - head is 2 

# 2
#  - perfectList is 2 -> None 
# - head is 1 


# 3 
# - perfectList is 1 -> 2 -> None 
# - head is 1 


def deleteDuplicates(head: ListNode) -> ListNode:

    if not head:
            return head 

    perfectList = deleteDuplicates(head.next)
    head.next = perfectList 
    # key insight to clean this up is that I can ALWAYS
    # attach head.next to the return value of the function 
    # I just will return one or the other, so the conditional attaching doesn't
    # really matter 

    if perfectList and perfectList.val == head.val: 
        return perfectList 
    else: 
        return head
    


    # assuming we're getting a perfect list back with no dupes
    # since it's sorted, we should check cur against our head that returns 
    # if they are the same we return the head we got 
    # if they are different we tie them and return new head (head) 




  
# arr = [1, 1, 2, 3, 3] 


#         x, y, z 
# arr = [1,1,2]


# [1, 1]




# dummyHead = ListNode(None, None)
# prevNode = dummyHead 

# for i in range(len(arr)):
#     node = ListNode(arr[i])     
#     prevNode.next = node 
#     prevNode = node 


# test = deleteDuplicates(dummyHead.next)

