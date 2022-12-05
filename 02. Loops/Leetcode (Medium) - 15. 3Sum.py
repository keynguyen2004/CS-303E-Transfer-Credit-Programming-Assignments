"""
Leetcode Problem #: 15
Leetcode Problem: 3Sum
Difficulty: Medium

If a + b + c == 0, then a + b = -c. This reduces the 3sum problem to
the 2Sum problem
"""

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range (len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            cur = nums[i]
            total = 0 - cur
            start, end = i + 1, len(nums) - 1

            while start < end:

                if nums[start] + nums[end] < total:
                    start += 1
                elif nums[start] + nums[end] > total:
                    end -= 1
                else:
                    res.append([cur, nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]:
                        start += 1
                    while start < end and nums[end] == nums[end + 1]:
                        end -= 1
                    
        return res

"""
Leetcode Problem #: 16
Leetcode Problem: 3Sum Closest
Difficulty: Medium

Similar to the previous problem, we also use the same approach
with two loops. However, we also need to keep track of the closest
difference between the target and the 3Sum.
"""

class Solution:
    def threeSumClosest(self, nums, target):
        nums.sort()
        closest = float("inf")

        for i in range (len(nums) - 2):

            if i > 0 and nums[i] == nums[i - 1]:
                continue
            start, end = i + 1, len(nums) - 1

            while start < end:
                
                total = nums[i] + nums[start] + nums[end]

                if abs(closest - target) > abs(total - target):
                    closest = total
                    if closest == target:
                        return closest

                if total < target:
                    start += 1
                    while nums[start] == nums[start - 1] and start < end:
                        start += 1
                else:
                    end -= 1
                    while nums[end] == nums[end + 1] and start < end:
                        end -= 1

        return closest