"""
Leetcode Problem #: 322
Leetcode Problem: Coin Change 
Difficulty: Medium

Suppose we have coins = {1 , 2 , 5 , 10 ... C}, index = 0 , 1 , 2 , 3 ... i.
Consider the last coin[i] = C, we either use it at least once or don't use it 
at all.

    a. If we use it at least once, the amount of money decrease by C, amount -= C
    b. If we don't use it at all, the amount of money stay the same, but the coin 
       we use becomes coins = 1 , 2 , 5 , 10 ... C-1, index = 0 , 1 , 2 , 3 ... I-1
 
Therefore, the DP representation would be

    1. Create an array(DP) of size amount + 1 to store the min number of coins 
       need to fulfill that amount, we start from 1 till the amount it self.
    2. The outer for loop is for the amount and inner for loop is to choose coins 
       to fulfill that amount
    3. Check if the current coin minus the amount is positive then we update it,
    4. This is the core of problem, dp[i] = min(dp[i], dp[i - coin] + 1) means the 
       minimum number of coins for the sum is minimum of all the different coins from
       coins list plus the that coin itself
    5. Finally, check if the dp[amount] was updated and return the dp[amount] else 
       return -1 (as the given list of coins was not able to fulfill the amount)
"""

class Solution:
    def coinChange(self, coins, amount):
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range (coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        return dp[amount] if dp[amount] != float("inf") else -1

    # This problem can encode using DFS approach

    def coinChange(self, coins, amount):
        coins.sort(reverse = True)
        
        dp = float("inf")
        def dfs(numberOfCoin, remainingAmount, index):
            nonlocal dp
            if remainingAmount < 0:
                return 
            if remainingAmount == 0:
                dp = min(dp, numberOfCoin)
                return 
            for i in range(index, len(coins)):
                sumOfCoin = dp - numberOfCoin
                if coins[i] * sumOfCoin > remainingAmount:
                    dfs(numberOfCoin + 1, remainingAmount - coins[i], i)

        dfs(0, amount, 0)
        return -1 if dp == float("inf") else dp

