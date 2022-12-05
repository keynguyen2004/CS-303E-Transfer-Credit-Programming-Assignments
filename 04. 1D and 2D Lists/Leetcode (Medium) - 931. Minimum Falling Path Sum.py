"""
Leetcode Problem #: 931
Leetcode Problem: Minimum Falling Path Sum
Difficulty: Medium 

The minimum path to get to element matrix[i][j] is the minimum of

    1. Diagonaly left: matrix[i - 1][j - 1] 
    2. Directly above: matrix[i - 1][j]
    3. Diagonaly right: matrix[i - 1][j + 1]

Starting from row 1, we add the minumum path to each element.
At the end,the smallest number in the last row is the miminum 
path sum.
"""

class Solution:
    def minFallingPathSum(self, matrix):
        row = len(matrix)
        col = len(matrix[0])

        for i in range(1, row):
            for j in range(col):
                move = []

                if j >= 1:
                    move.append(matrix[i-1][j-1])
                if j < col - 1:
                    move.append(matrix[i-1][j+1])

                move.append(matrix[i-1][j])
                matrix[i][j]+=min(move)

        return min(matrix[-1])



# We can also a recursive solution which traversal the matrix from
# top to bottom

class Solution:
    def minFallingPathSum(self, matrix):

        def recursion(matrix, i, j):
            import sys

            if i == len(matrix):
                return 0

            curSum, minSum = 0, sys.maxint
            path = (j - 1, j, j + 1)

            for move in path:
                if 0 <= move <= len(matrix[0]) - 1:
                    current_sum = recursion(matrix, i + 1, move)
                    minSum = min(minSum, curSum + matrix[i][j])
            return minSum
        
    
        for j in range(len(matrix[0])):
            val = recursion(matrix, 0, j)
            res = min(res, val)
        return res