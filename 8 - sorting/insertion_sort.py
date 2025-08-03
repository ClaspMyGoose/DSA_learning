

# instincts say I need a second pointer 
# instincts are right, I just blind myself lol 

# remember the trick, how do we make it so we're just 
# continuously looking at one thing at a time 



def insertion_sort(arr: list) -> list: 



    # first element already sorted 

    # start with # 2 

    # move through the array with a for loop 
    # and use j as our pointer to move 
    # an unsorted element back through the array 
    # one index at a time 
    for i in range(1, len(arr)):
        j = i - 1 
        
        # make sure j stays in bounds
        # and keep swapping as long as 
        # j is greater than the element to the right  
        while j >= 0 and arr[j] > arr[j + 1]:
            # to swap the vars I need a tmp 
            tmp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = tmp 
            j -= 1 


    return arr 




arr = [2,3,4,6,1]

insertion_sort(arr)