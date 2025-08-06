
# ! key takeaways here 

# I got it to work doing a check between first and last index on every row 

# this essentially uses similar principles but different structure in the row-wise binary search at the beginning 

# if below first we look at earlier rows 

# if after last we look at later rows 

# in practice, mid will be the value we want using this logic, unless our top and bottom pointers cross over in which case we know to exit 



def bin_search_2D(matrix: list[list[int]], target: int) -> bool: 
    


    top, bot = 0, len(matrix) - 1

    while top <= bot:
        
        mid = (top + bot) // 2

        if target < matrix[mid][0]:
            bot = mid - 1
        elif target > matrix[mid][-1]:
            top = mid + 1 
        
        # i.e. loop will stop if our value is inbetween 
        else: 
            break 
    
    # possible for pointers to cross over if our target is 
    # below value at first ind of first row 
    # or above value at last ind of last row 

    if not (top <= bot):
        return False 


    arr = matrix[mid]
    left, right = 0, len(arr) - 1

    while left <= right: 
        mid = (left + right) // 2


        if target > arr[mid]:
            left = mid + 1 
        elif target < arr[mid]:
            right = mid - 1 
        else:
            return True 
    
    return False 



input = [[1,2,4,8],[10,11,12,13],[14,20,30,40]]
target = 1
target = 30 

# input=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# target=3

input = [[1],[3]]
target = 0

bin_search_2D(input, target)


'''
[1,2,4,8]
[10,11,12,13]
[14,20,30,40]
'''