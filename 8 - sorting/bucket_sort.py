# Sort Colors 


def sortColors(self, nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    
    # nums is a list 
    # index of distro = color key 
    distro = [0,0,0] 

    for i in range(len(nums)):
        distro[nums[i]] += 1

    
    fill_ptr = 0 

    # distro = [1,2,1]

    for i in range(len(distro)):
        key_count = distro[i]
        for j in range(key_count):
            nums[fill_ptr] = i 
            fill_ptr += 1 