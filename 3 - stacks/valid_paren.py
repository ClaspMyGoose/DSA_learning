# 20. Valid Parentheses
# Easy
# Topics
# premium lock icon
# Companies
# Hint
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"

# Output: true

# Example 2:

# Input: s = "()[]{}"

# Output: true

# Example 3:

# Input: s = "(]"

# Output: false

# Example 4:

# Input: s = "([])"

# Output: true

# Example 5:

# Input: s = "([)]"

# Output: false

 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.



# ! first solution, this works but on further examination we can simplify 


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s) % 2 != 0:
        return False 
        
    stack = [] 

    matchingDict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }


    for i in range(len(s)): 
        if matchingDict.get(s[i]):
            stack.append(s[i])
        else: 
            
            # TODO NESTED IFs, both returning FALSE ====== AND 
            if len(stack) > 0:
            
                if s[i] == matchingDict[stack[len(stack) - 1]]:
                    stack.pop()
                else:
                    return False 
            else:
                return False 
            

    # TODO since we're doing this check to make sure the stack was exhausted we don't need our modulo check up top. This will guarantee even number of char 
    if len(stack) == 0:
        return True 
    else:
        return False 
        


# ! Second implementation with issues from first corrected 

def isValid2(s):
    """
    :type s: str
    :rtype: bool
    """
        
    stack = [] 

    matchingDict = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    # TODO  I can simplify some of my language to be more pythonic tho 
    for i in range(len(s)): 
        if matchingDict.get(s[i]):
            stack.append(s[i])
        else: 
            if len(stack) > 0 and s[i] == matchingDict[stack[len(stack) - 1]]:
                stack.pop()
            else:
                return False 
            
    if len(stack) == 0:
        return True 
    else:
        return False 

# ! third implementation basically makes the above solution a lot more pythonic 
# funny how I use a lot of these conventions until we start to get technical with the DSA
# then my brain throws out all the easy conventions 

def isValid3(s): 
    
    stack = []
    hashmap = {
        '(': ')',
        '[': ']',
        '{': '}'
    }

    for char in s:
        
        if char in hashmap: 
            stack.append(char)
        else: 
            if stack and hashmap[stack[-1]] == char:
                stack.pop()
            else:
                return False 
    
    if stack:
        return False 

    return True 