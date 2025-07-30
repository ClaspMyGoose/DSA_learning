# 707. Design Linked List
# Medium
# Topics
# premium lock icon
# Companies
# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

# Implement the MyLinkedList class:

# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.
 

# Example 1:

# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]

# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
 

# Constraints:

# 0 <= index, val <= 1000
# Please do not use the built-in LinkedList library.
# At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.


# ! Still not working. I'm close but still failing on specific edge cases 
# 66/76 passed 


import sys 


class ListNode: 
    def __init__(self, val, next=None):
        self.val = val
        self.next = next 


class MyLinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None 
        self.length = 0


    def get(self, index: int) -> int:
        
        # what ways could the index be invalid? It will definintely be a number 
        # if self.length = 0 (i.e. nothing in our linked list)
        # if index >= self.length 
        # if index < 0 
        # bad condition 
        if not self.length or index >= self.length or index < 0:
            return -1
        
        else: 
            cur = self.head 
            while index: 
                cur = cur.next 
                index -= 1
        test = self.validate_length()
        if not test:
            sys.exit()
        return cur.val
            # march through our nodes in a while loop until index is exhausted 




    def addAtHead(self, val: int) -> None:
        
        node = ListNode(val)
        # not started 
        if not self.length: 
            self.head = node
            self.head.next = None 
            self.length += 1 
            self.tail = node 
        else: 
            old_head = self.head 
            self.head = node 
            self.head.next = old_head
            if self.length == 1:
                self.tail = old_head
            self.length += 1

        test = self.validate_length()
        if not test:
            sys.exit()

    def addAtTail(self, val: int) -> None:

        # should be pretty easy because of tail pointer
        # similar defensive checks as addAtHead 
        node = ListNode(val)

        if not self.length: 
            # if completely empty, add and set as head and tail 
            self.head = node 
            self.head.next = None 
            self.tail = node 
            self.length += 1 
        else: 
            old_tail = self.tail 
            old_tail.next = node
            self.tail = node
            self.tail.next = None  
            self.length += 1
            
            # otherwise I think we should just be safe to do the thing
        
        test = self.validate_length()
        if not test:
            sys.exit()

        

    def addAtIndex(self, index: int, val: int) -> None:

        # similar defenses as before 
        # valid range would be 0 - length of list (gets added at end)
        if index < 0 or index > self.length: 
            return 

        if index == 0:
            self.addAtHead(val)
        
        elif index == self.length:
            self.addAtTail(val)

        #we need to stop 1 BEFORE the node that is shifting to make this easier 
        else: 

            node = ListNode(val)
            cur = self.head
            dummyIndex = index - 1


            while (dummyIndex):
                cur = cur.next
                dummyIndex -= 1
            
            # cur should now be the node prior to our insert 
            old_next = cur.next 
            cur.next = node 
            node.next = old_next
            self.length += 1  

        test = self.validate_length()
        if not test:
            sys.exit()

        

    def deleteAtIndex(self, index: int) -> None:
        
        # let's think about our states 
        # empty 
        # length of 1 
        # deleting head or tail? 
        if index < 0 or index >= self.length: 
            return 


        cur = self.head
        steps = index - 1
        
        
        # [1,2,3]

        # if 0 , I'm stopping at my deletion here 
        # if anything else, I'm stopping one before my deletion 

        while steps > 0:
            cur = cur.next 
            steps -= 1
        
        if cur == self.head and cur == self.tail: 
            self.head = None 
            self.tail = None 
            # do work, update self.head and self.tail 
        elif cur == self.head:
             self.head = cur.next 
            # do work update self.head 
        elif cur.next == self.tail: 
            new_next = cur.next.next 
            cur.next = new_next
            self.tail = cur 
        else:
            new_next = cur.next.next 
            cur.next = new_next
            # do work, no local updates  
            
        self.length -= 1
        test = self.validate_length()
        if not test:
            sys.exit()
        # can we use the look ahead? cur.next.next? 


    def print_list(self):
        """Helper function to visualize the list"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        print(f"List: {result}, Length: {self.length}, Head: {self.head.val if self.head else None}, Tail: {self.tail.val if self.tail else None}")


    def validate_length(self):
    # Count actual nodes
        actual = 0
        current = self.head
        while current:
            actual += 1
            current = current.next
        
        if actual != self.length:
            print(f"LENGTH MISMATCH! Actual: {actual}, Tracked: {self.length}")
            return False
            
        return True


def setup_debug_list():
    ll = MyLinkedList()
    
    # Build the exact list: [9, 76, 8, 22, 73, 31, 80, 37, 33, 16, 1, 14, 17, 84, 8, 0, 80, 2, 23, 53, 90, 98, 19, 12, 43, 17, 21, 14, 50, 28]
    values = [76, 8, 97, 22, 73, 31, 80, 37, 33, 16, 1, 14, 17, 84, 8, 0, 80, 2, 23, 53, 98, 19, 12, 43, 17, 21, 37, 14, 50, 28, 79]
    
    for val in values:
        ll.addAtTail(val)
    
    return ll

# # Usage:
# ll = setup_debug_list()
# ll.deleteAtIndex(30)
# ll.addAtTail(5)


# ll.print_list()  # Should show length 30, not 33!

# print(f"Trying to delete index 30 from list of length {ll.length}")
# print(f"Index 30 is {'valid' if 30 < ll.length else 'INVALID'}")

# Now you can debug the deleteAtIndex call
# ll.deleteAtIndex(30)

operations = ["MyLinkedList","addAtHead","addAtIndex","addAtTail","addAtTail","addAtTail","addAtIndex","addAtTail","addAtHead","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtIndex","addAtTail","get","get","addAtHead","addAtTail","addAtTail","get","addAtTail","addAtTail","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","addAtIndex","get","addAtTail","addAtIndex","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtIndex","addAtHead","addAtIndex","addAtTail","addAtHead","addAtIndex","addAtTail","addAtHead","deleteAtIndex","get","addAtIndex","get","addAtIndex","addAtTail","addAtTail","get","deleteAtIndex","get","addAtHead","addAtTail","addAtIndex","addAtIndex","addAtIndex","addAtHead","addAtTail","addAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtTail","get","addAtTail","addAtIndex","addAtHead","deleteAtIndex","addAtHead","deleteAtIndex","get","get","addAtTail","addAtIndex","get","deleteAtIndex","deleteAtIndex","addAtHead","addAtHead","addAtIndex","get","addAtTail","addAtHead","addAtIndex","get","addAtHead","deleteAtIndex","deleteAtIndex","deleteAtIndex","addAtHead","addAtTail","get","addAtHead","addAtTail","addAtHead","addAtHead","deleteAtIndex","get","addAtHead"]
arguments = [[],[55],[1,90],[51],[91],[12],[2,72],[17],[82],[4],[7],[7],[5,75],[54],[6],[2],[8],[35],[36],[10],[40],[43],[12],[3],[78],[89],[3,41],[10],[96],[5,37],[51],[26],[16,91],[18],[11],[66],[22,20],[44],[17,16],[95],[2],[14,2],[99],[51],[1],[11],[22,99],[20],[25,42],[72],[45],[2],[4],[32],[55],[84],[32,64],[26,14],[30,80],[88],[51],[27,71],[15],[8],[60],[37],[25],[96],[25,53],[36],[8],[85],[42],[20],[34],[78],[42,76],[26],[30],[39],[27],[93],[19,75],[8],[24],[32],[25,98],[21],[95],[18],[45],[24],[38],[8],[20],[83],[71],[78],[55],[29],[11],[84]]


# operations = ["MyLinkedList","addAtHead","addAtTail","addAtTail","get","get","addAtTail","addAtIndex","addAtHead","addAtHead","addAtTail","addAtTail","addAtTail","addAtTail","get","addAtHead","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtTail","deleteAtIndex","addAtHead","addAtHead","addAtIndex","addAtTail","get","addAtIndex","addAtTail","addAtHead","addAtHead","addAtIndex","addAtTail","addAtHead","addAtHead","get","deleteAtIndex","addAtTail","addAtTail","addAtHead","addAtTail","get","deleteAtIndex","addAtTail","addAtHead","addAtTail","deleteAtIndex","addAtTail","deleteAtIndex","addAtIndex","deleteAtIndex","addAtTail","addAtHead","addAtIndex","addAtHead","addAtHead","get","addAtHead","get","addAtHead","deleteAtIndex","get","addAtHead","addAtTail","get","addAtHead","get","addAtTail","get","addAtTail","addAtHead","addAtIndex","addAtIndex","addAtHead","addAtHead","deleteAtIndex","get","addAtHead","addAtIndex","addAtTail","get","addAtIndex","get","addAtIndex","get","addAtIndex","addAtIndex","addAtHead","addAtHead","addAtTail","addAtIndex","get","addAtHead","addAtTail","addAtTail","addAtHead","get","addAtTail","addAtHead","addAtTail","get","addAtIndex"]

# arguments = [[],[84],[2],[39],[3],[1],[42],[1,80],[14],[1],[53],[98],[19],[12],[2],[16],[33],[4,17],[6,8],[37],[43],[11],[80],[31],[13,23],[17],[4],[10,0],[21],[73],[22],[24,37],[14],[97],[8],[6],[17],[50],[28],[76],[79],[18],[30],[5],[9],[83],[3],[40],[26],[20,90],[30],[40],[56],[15,23],[51],[21],[26],[83],[30],[12],[8],[4],[20],[45],[10],[56],[18],[33],[2],[70],[57],[31,24],[16,92],[40],[23],[26],[1],[92],[3,78],[42],[18],[39,9],[13],[33,17],[51],[18,95],[18,33],[80],[21],[7],[17,46],[33],[60],[26],[4],[9],[45],[38],[95],[78],[54],[42,86]]

# Run the test
ll = None
results = []

for i, (op, args) in enumerate(zip(operations, arguments)):
    print(f"\nStep {i}: {op}({args})")
    
    if op == "MyLinkedList":
        ll = MyLinkedList()
        results.append(None)
    elif op == "addAtHead":
        ll.addAtHead(args[0])
        results.append(None)
    elif op == "addAtTail":
        ll.addAtTail(args[0])
        results.append(None)
    elif op == "addAtIndex":
        ll.addAtIndex(args[0], args[1])
        results.append(None)
    elif op == "get":
        result = ll.get(args[0])
        results.append(result)
        print(f"  -> get returned: {result}")
    elif op == "deleteAtIndex":
        print(f'Running Delete At Index: {i}')
        print(f'Args are: {args[0]}')
        ll.deleteAtIndex(args[0])
        results.append(None)
    
    # Print current state after each operation
    if ll:
        ll.print_list()
    
    # Stop if we hit an error early for debugging
    if i > 100:  # Adjust this number to see more or fewer steps
        break

print("\nFinal results:", results)



