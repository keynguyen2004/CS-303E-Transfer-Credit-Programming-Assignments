"""
Leetcode Problem #: 11
Leetcode Problem: Container With Most Water
Difficulty: Medium

For this problem, we will use the two pointers approach with start and 
end pointers at both ends of the array. We then loop from either ends 
until the two pointers meet, and while looping through the array, we 
can calculate the water area and compare it with the current maximum area.
"""


class Solution:
    def maxArea(self, height):
        if len(height) == 2:
            return min(height)

        start, end, maxWater = 0, len(height) - 1, 0
        while start < end:

            maxWater = max(min(height[start], height[end])*(end - start),
                           maxWater)

            if height[start] < height[end]:
                start += 1
            else:
                end -= 1

        return maxWater

        
# We can optimize the solution a little bit further by placing while 
# loop after the increment of start and the decrement of end so that 
# the pointer will reach the index where the container height is greater 
# than the current height

class Solution:
    def maxArea(self, height):
        if len(height) == 2:
            return min(height)

        start, end, maxWater = 0, len(height) - 1, 0
        while start < end:

            minimumHeight = min(height[start], height[end])
            area = minimumHeight * (end - start)
            maxWater = max(area, maxWater)

            if height[start] < height[end]:
                start += 1
                while height[start] < minimumHeight:
                    start += 1
            else:
                end -= 1
                while height[end] < minimumHeight:
                    end -= 1

        return maxWater