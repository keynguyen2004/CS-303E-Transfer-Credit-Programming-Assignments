"""
Leetcode Problem #: 1047
Leetcode Problem: Remove All Adjacent Duplicates In String
Difficulty: Easy

To begin with, we will tackle the easier version of this problem
where you will only need to remove two adjacent duplicate letters
from the string until there's no more such pair.
"""

class Solution:
    def removeDuplicates(self, s):

        stack = []
        
        for char in s:
            if stack and stack[-1] == char:
                stack.pop()
            else:
                stack.append(char)
        
        return "".join(stack)
       
"""
Leetcode Problem #: 1209
Leetcode Problem: Remove All Adjacent Duplicates In String II
Difficulty: Medium

Now, we will do the same and remove k adjacent duplicates, which 
we'll use a 2D array to store the character and the number of 
adjacent duplicates as we loop through each character of the string
"""

class Solution:
    def removeDuplicates(self, s, k):
        
        stack = []

        for char in s:
            if stack and stack[-1][0] == char:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([char, 1])
        
        return "".join(x * y for x, y in stack)