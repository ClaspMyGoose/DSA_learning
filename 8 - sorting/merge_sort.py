


def merge_sort(arr):
    
    if not arr:
        return arr 
    

    # don't care whether larger portion goes left or right 
    # so this simplifies to len(arr) // 2 
    # halfway = len(arr) // 2 
    # odd_adjust = len(arr) % 2 
    # indices = halfway + odd_adjust 
    
    mid = len(arr) // 2

    if len(arr) == 1:
        return arr
    else: 
        left = merge_sort(arr[:mid])
        right = merge_sort(arr[mid:])
        

    left_p = 0 
    right_p = 0 

    for i in range(len(arr)): 
        if right_p == len(right) or (left_p < len(left) and left[left_p] < right[right_p]):
            arr[i] = left[left_p]
            left_p += 1
        else:
            arr[i] = right[right_p]
            right_p += 1 


    return arr 
    
           
arr = [2, 1]
arr = [2,3,1]
arr = [2,3,4,6,1]



merge_sort(arr)




# let's think about this 

# base case = array of length 1 




# at each level we have a 

# arr that we are trying to fill 


# left_p = 0

# right_p  = 0 


# for i in range(len(arr)): 
#     if left_p < len(left) and left[left_p] < right[right_p]:
#         arr[i] = left[left_p]
#         left_p += 1
#     else:
#         arr[i] = right[right_p]
#         right_p += 1 