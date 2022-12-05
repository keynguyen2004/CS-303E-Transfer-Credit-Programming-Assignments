"""
Leetcode Problem #: 1
Leetcode Problem: Two Sum
Difficulty: Easy

To begin with, we could approach this problem using a
brute force solution where we use 2 for loops to locate
a number (first for loop) and its complementary (second 
for loop) which add up to the target number
"""

# Brute force solution
# Time complexity: O(n^2)

class Solution:
    def twoSum(self, nums, target):
        n = len(nums)

        for i in range (n):
            for j in range (i + 1, n):
                if nums[i] + nums[j] == target:
                    return [nums[i], nums[j]]


# However, we can optimize this solution using a dictionary
# to store, at a particular index, the number at that index 
# and the complementary number needed so that their sum equals
# the target number.
# Time complexity: O(n)

class Solution:
    def twoSum(self, nums, target):
        dic = {}

        for i in range (len(nums)):
            if nums[i] in dic:
                return [dic[nums[i]], i]
            else:
                dic[target - nums[i]] = i
            