# Remove Element
# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

# Note:

# The order of the elements which are not equal to val does not matter.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain only elements not equal to val.
# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4], val = 1

# Output: [2,3,4]
# Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2

# Output: [0,1,3,0,4]
# Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100



# took me a little bit to formulate but I knew I was overcomplicating so sat with it for a bit 




def removeElement(nums: list[int], val: int) -> int:
    

    left = 0 

    for right in range(len(nums)):
        
        if nums[right] != val:
            nums[left] = nums[right]
            left += 1
    return left

# Input: nums = [1,1,2,3,4], val = 1

'''

3rd loop 
left = 0
right = 2 

nums[right] = 2 







'''




         
             



