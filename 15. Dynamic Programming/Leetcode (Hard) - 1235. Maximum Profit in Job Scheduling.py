"""
Leetcode Problem #: 1235
Leetcode Problem: Maximum Profit in Job Scheduling 
Difficulty: Hard

This problem follows a classical 0/1 Knapsack pattern, namely, optimizing 
the sum of weights for a list of items given that either of the items can 
be included/excluded. This straightforwardly translates into a dynamic 
programming algorithm where on each iteration we
  
    0. Either go straight to the next job and skip this one,
    1. Or include the current job and then try the next one.

In this problem, the constraint is that the next interval should not overlap 
with the current one. Thus, when considering branch "1" of 0/1 -Knapsack 
(i.e., include item), we should rephrase the condition:

    1. Include the current item (job) and then try the next valid (non-overlapping) one.
"""

class Solution:
    def jobScheduling(self, startTime, endTime, profit):
        from bisect import bisect_left

        # Bundle the three lists together and sort them by the start time
        jobs, n = sorted(zip(startTime, endTime, profit)), len(startTime)
        dp = [0] * (n + 1)

        for i in reversed(range(n)):
            k = bisect_left(jobs, jobs[i][1], key = lambda time:time[0])

            # 0/1 Knapsack: EITHER choose the next job 
            # OR choose the current job and the next valid one
            dp[i] = max(jobs[i][2] + dp[k], dp[i + 1])
        return dp[0]

    # Alternatively, we can encode the problem using DFS

    def jobScheduling(self, startTime, endTime, profit):
        from bisect import bisect_left

        jobs = sorted(zip(startTime, endTime, profit))
    
        def dfs(i):
            if i >= len(jobs):
                return 0

            k = bisect_left(jobs, jobs[i][1], key = lambda time: time[0])
            return max(dfs(i+1), jobs[i][2] + dfs(k))
        
        return dfs(0)
