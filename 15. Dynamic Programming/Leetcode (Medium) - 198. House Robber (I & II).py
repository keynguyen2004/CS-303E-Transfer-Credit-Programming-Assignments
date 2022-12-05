"""
Leetcode Problem #: 198
Leetcode Problem: House Robber 
Difficulty: Medium

This problem follows the 0/1 Knapsack pattern, where we are trying to
optimize the stolen amount by 

    1. EITHER stole the current house, then the value is: dp[i] = dp[i-2] + arr[i],
       because you cannot stole the previous house;
    2. OR don't stole from the current house, and keep the previous value, dp[i] = dp[i-1];
       the target is to keep the maximum value, so dp[i] = max(dp[i-1], dp[i-2] + arr[i])

We create the variables prev2, prev, cur, which correspond with dp[i - 2], dp[i - 1], dp[i]
"""

class Solution:
    def rob(self, nums):
        prev2, prev, cur = 0, 0, 0
        for house in nums:
            cur = max(prev, house + prev2)
            prev2 = prev
            prev = cur
        return cur
    
    # The shortened version
    def rob(self, nums):
        prev, cur = 0, 0
        for house in nums:
            prev, cur = cur, max(cur, house + prev)
        return prev


"""
Leetcode Problem #: 213
Leetcode Problem: House Robber II
Difficulty: Medium

Extended from the previous problem, we have two sub-problems

    1. Maximum value we can rob using house 0 to n-2
    2. Maximum value we can rob using house 1 to n-1

"""

class Solution:
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        def robHouse(arr):
            prev, curr = 0, 0
            for house in arr:
                prev, curr = curr, max(curr, house + prev)
            return curr
        
        rob_first = robHouse(nums[:len(nums)])
        rob_last = robHouse(nums[1:])

        return max(rob_first, rob_last)