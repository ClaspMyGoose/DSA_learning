
# Concatenation of Array
# Solved 
# You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:

# Input: nums = [1,4,1,2]

# Output: [1,4,1,2,1,4,1,2]
# Example 2:

# Input: nums = [22,21,20,1]

# Output: [22,21,20,1,22,21,20,1]
# Constraints:

# 1 <= nums.length <= 1000.
# 1 <= nums[i] <= 1000


# fairly straightforward 


def getConcatenation(nums: list[int]) -> list[int]:
        
        # nums 
        # [1, 4, 1, 2]

        ans = []
        # len = 4 

        # starts at 0 
        for i in range(2 * len(nums)):
            if i >= len(nums): 
                # need to add to it
                ans.append(nums[i - len(nums)]) 
            else:
                ans.append(nums[i])
        return ans 



getConcatenation([1,4,1,2])