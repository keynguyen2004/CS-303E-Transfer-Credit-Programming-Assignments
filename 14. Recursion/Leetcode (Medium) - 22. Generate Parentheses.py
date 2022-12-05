"""
Leetcode Problem #: 22
Leetcode Problem: Generate Parentheses
Difficulty: Medium

We can see the recursive pattern where we choose to add either 
an open bracket or a close bracket. This can be implemented as 
part of the recursive call, which you don't add a close bracket 
if there isn't already an open bracket
"""

class Solution(object):
    def generateParenthesis(self, n):
        
        def recursion(opened, closed, parentheses, res):
			# evaluate current string
			# if we are out of brackets to add, we must be at a valid string
            if opened == 0 and closed == 0:
                res.append(parentheses)
                return

			# recursive call: add either open or close
			# if adding open bracket is valid
            if opened > 0:
				# add open bracket, decrease count
                recursion(opened - 1, closed, parentheses + "(", res)

			# if adding close bracket is valid
            if closed > opened:
				# add close bracket, decrease count
                recursion(opened, closed - 1, parentheses + ")", res)
            
            
            return res
            
        res = recursion(n, n, '', [])
        
        return res

# Alternatively, this can be implemented using DFS

class Solution:
    def generateParenthesis(self, n):
        
        res = []

        def dfs(opened, closed, parentheses):
            if len(parentheses) == 2 * n:
                res.append(parentheses)
                return
            
            if opened > closed:
                dfs(opened, closed + 1, parentheses + ")")
            if opened < n:
                dfs(opened + 1, closed, parentheses + "(")

        dfs(0, 0, "")
        return res