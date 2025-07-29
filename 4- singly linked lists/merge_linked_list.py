

# ! key insight here is that the use of a dummy list helps a bunch 
# I knew how to approach (while loop to consume both lists), but wasn't sure how to 
# get started before I thought of an initial dummy node to chain everything to 


# ! Claude's advice: 

'''
# ! I ALMOST DID THIS AND THOUGHT BETTER OF IT, basically handling the first node manually 
# ! basically the same idea as a dummy node just not as elegant 
1. Just start with the messiest version first
When you're stuck on setup, write the ugly version:
python# I know this is messy but let me just START
if list1.val <= list2.val:
    result = list1
    list1 = list1.next
else:
    result = list2
    list2 = list2.next

current = result
# Now do the main loop...
Sometimes seeing the ugly code helps you realize "oh, a dummy node would clean this up!"

2. Use placeholder patterns
When stuck, literally write:
python# TODO: figure out how to start this thing
result = "somehow pick the first node"
current = result
while list1 and list2:
    # I know this part works


# ! I just need to learn / practice these to death over the rest of this year  
3. Practice the "common setup patterns"

Dummy nodes for building lists
Two pointers starting at different positions
Sentinel values for edge cases


'''


# 21. Merge Two Sorted Lists
# Solved
# Easy
# Topics
# premium lock icon
# Companies
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
 

# Constraints:

# The number of nodes in both lists is in the range [0, 50].
# -100 <= Node.val <= 100
# Both list1 and list2 are sorted in non-decreasing order.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1, list2):
    

        dummyNode = ListNode(None, None)
        dummyNodeHead = dummyNode

        while list1 and list2:
            if list1.val <= list2.val:
                dummyNode.next = list1
                list1 = list1.next 
            else: 
                dummyNode.next = list2
                list2 = list2.next 
            dummyNode = dummyNode.next
        
        if list1 and not list2: 
            dummyNode.next = list1
        elif list2 and not list1:
            dummyNode.next = list2 
        else: 
            pass 

        return dummyNodeHead.next 