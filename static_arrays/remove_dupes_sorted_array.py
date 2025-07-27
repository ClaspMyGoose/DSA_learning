# Remove Duplicates From Sorted Array
# You are given an integer array nums sorted in non-decreasing order. Your task is to remove duplicates from nums in-place so that each element appears only once.

# After removing the duplicates, return the number of unique elements, denoted as k, such that the first k elements of nums contain the unique elements.

# Note:

# The order of the unique elements should remain the same as in the original array.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain all the unique elements.
# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4]

# Output: [1,2,3,4]
# Explanation: You should return k = 4 as we have four unique elements.

# Example 2:

# Input: nums = [2,10,10,30,30,30]

# Output: [2,10,30]
# Explanation: You should return k = 3 as we have three unique elements.

# Constraints:

# 1 <= nums.length <= 30,000
# -100 <= nums[i] <= 100
# nums is sorted in non-decreasing order.


def removeDuplicatesCheating(self, nums: list[int]) -> int:

        # technically doesn't count because we allocate extra space 
        # for another array here 
        lastSeen = None
        solutionArr = []

        for num in nums:
            if num != lastSeen:
                solutionArr.append(num)
                lastSeen = num 
        
        k = len(solutionArr)
        for i in range(len(solutionArr)):
            nums[i] = solutionArr[i]

        return k 




def removeDuplicatesTimeout(nums: list[int]) -> int:
        
        # nums is sorted in increasing order = [1,3,5]
        
        # unique number counter 
        k = 0  
        # last number seen 
        lastSeen = None

        # index pointers 
        left = 0 
        cur = 0 

        while left < len(nums):
            
            if nums[left] != lastSeen:
                nums[cur] = nums[left]
                lastSeen = nums[left]
                k += 1 
                left += 1
                cur += 1
            else:
                while nums[left] == lastSeen and nums[left] < len(nums):
                    lastSeen = nums[left]
                    left += 1

                if nums[left] != lastSeen:
                    nums[cur] = nums[left]
                    lastSeen = nums[left]
                    k += 1
                    left += 1
                    cur += 1
                 
        return k 

# ! key insight here is that the array is sorted in increasing order
# ! so we can determine a "dupe" by just looking at the current number and the previous number
# ! helps to simplify the logic, at least in my head. Before I saw this clearly I was overcomplicating                
def removeDuplicates(nums: list[int]) -> int:
    
    left = 1
    right = 1 

    while right < len(nums):
        # non dupe, store in left and increment both 
        if nums[right] != nums[right - 1]:
            nums[left] = nums[right]
            left += 1
            right += 1
        else:
            right += 1
    
    return left




removeDuplicates([1,1,2,3,4])

