

# ! solution works on NeetCode but LeetCode wants something else
# ! timing out on the two-branch 

def climbStairs(n: int) -> int:

# n number of steps to reach the top 

        # I can either take 1 or 2 steps at each level
        # two branch recursion 

        if n < 0:
            return 0
        elif n <= 1:
            return 1  
        else: 
            solutions = 0
            solutions += (climbStairs(n - 1) + climbStairs(n - 2))
            return solutions

        # how do we define a "valid end"

        # start with something like 
        # n = 1 # 1 valid way (1 step) 
        # n = 2 # 2 valid ways (1 + 1 step, 2 step)
        # n = 3 # 3 valid ways (2 + 1, 1 + 1 + 1, 1 + 2)


        # general idea is we set off from each "step" 
        # trying to take 1 and 2 
        # if any given path reaches the end in a valid way
n = 3
#n = 2
#n = 1


climbStairs(n)




