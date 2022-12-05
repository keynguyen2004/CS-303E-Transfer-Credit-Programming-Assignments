"""
Leetcode Problem #: 120
Leetcode Problem: Triangle
Difficulty: Medium

We go from the top of the triangle down to the bottom row.
Since we can only visit index and index + 1 in the next level,
we can get the minimum sum from all the levels below a given 
level and an index [i][j]. For the last level the minimum sum 
would be the individual elements themselves. So create a 2D 
array which will store the answers that we have already calculated
for a given level and its index. 
"""


class Solution:
    def minimumTotal(self, triangle):

        for i in range (1, len(triangle)):
            for j in range (i + 1):

                if j == 0:
                    triangle[i][j] += triangle[i-1][j]
                elif j == i:
                    triangle[i][j] += triangle[i-1][j-1]
                else:
                    triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

        return min(triangle[-1])



# From the above solution, we can implement a recursive 
# solution with the line below 
# triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])


class Solution:
    def minimumTotal(self, triangle):  

        row = len(triangle)

        def recursion(i, j):
            if i == row - 1:
                return triangle[i][j]

            horizontal = triangle[i][j] + recursion(i + 1, j)
            diagonal = triangle[i][j] + recursion(i + 1, j + 1)

            return min(horizontal, diagonal)

        return recursion(0,0)