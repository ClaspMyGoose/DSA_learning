    # check end of each row first 

        # then we know which row to use and it's regular binary search 

def bin_search_2D(matrix: list[list[int]], target: int) -> bool: 
    
    


    # instead of the below, why can't we just check each row to see if our value is between or = to values? 
    row = -1  
    for i in range(len(matrix)): 
        
        if matrix[i][0] == target or matrix[i][len(matrix[i]) - 1] == target:
            return True 
        elif target > matrix[i][0] and target < matrix[i][len(matrix[i]) - 1]:
            row = i 
            break 
        else: 
            continue 


    
    if not row >= 0:
        return False 

    arr = matrix[row]
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

input=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target=3



bin_search_2D(input, target)


'''
[1,2,4,8]
[10,11,12,13]
[14,20,30,40]
'''