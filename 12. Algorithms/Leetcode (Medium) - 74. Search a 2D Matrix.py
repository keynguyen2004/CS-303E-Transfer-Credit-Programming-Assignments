"""
Leetcode Problem #: 74
Leetcode Problem: Search a 2D Matrix
Difficulty: Medium
"""

# To begin with, I did a linear search on the 2D matrix 
# to search for the target number. If it's not found and
# the linear search reach a number greater than the target
# return False.

class Solution:
    def searchMatrix(self, matrix, target):
        for i in range (len(matrix)):
            for j in range (len(matrix[0])):
                if matrix[i][j] < target:
                    continue
                elif matrix[i][j] > target:
                    return False
                else:
                    return True


# However, the solution can be ineffective for a large number of 
# row and column. Therefore, we can optimize by using a binary search
# for the last column of the 2D matrix to locate which row that (can)
# contains the target number. Then, perform the binary search again for 
# that particular row to find the target number

class Solution:
    def searchMatrix(self, matrix, target):
        row, col = len(matrix), len(matrix[0])
        low, high = 0, row - 1
        index = -1
        while low <= high:
            mid = (low + high)//2
            if matrix[mid][0] <= target and matrix[mid][col - 1] >= target:
                index = mid
                break
            elif matrix[mid][col - 1] > target:
                high = mid - 1
            else:
                low = mid + 1
           
        low, high = 0, col - 1
        while low <= high:
            mid= (low + high)//2
            if matrix[index][mid] == target:
                return True
            elif matrix[index][mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        return False
                