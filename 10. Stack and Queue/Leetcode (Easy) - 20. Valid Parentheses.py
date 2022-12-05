"""
Leetcode Problem #: 20
Leetcode Problem: Valid Parentheses 
Difficulty: Easy

For this problem, we will be using stacks.
We use list as stack in Python. In addition,
we will have 3 bracket catogories, 3 lists, ( ) [ ] { } 
If one bracket category is not close yet, we should 
not change to other category, so we can set a flag 
for the bracket category we are currently have.
"""

class Solution:
    def isValid(self, s):
        if len(s)%2 == 1:
            return False
        
        stack = []
        dic = {")":"(", "]": "[", "}": "{"}

        for char in s:
            if char in dic:
                if stack and dic[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)

        return len(stack) == 0



# We can also solve this problem without using stack by
# using Python string replacement function

class Solution:
    def isValid(self, s: str):
        if len(s)%2==1:
            return False

        dic = {")":"(", "]": "[", "}": "{"}       
        flag = True

        while flag == True:
            prevStr = s
            for parentheses in dic:
                s = s.replace(parentheses, '')

            if len(prevStr) > len(s):
                flag = True
            else:
                if len(s) == 0:
                    return True
                else:
                    return False