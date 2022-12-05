"""
Leetcode Problem #: 1534
Leetcode Problem: Count Good Triplets
Difficulty: Easy

For this problem, we can approach it following this method

    1. Firstly, we can modify the range of the list so that we 
       can loop through all the triplets. In that way, our first
       criteria is achieved 
    2. Secondly, we check the remaining criterias to see if they 
       applied for our triplets

From here, we use three (nested) for loops to find the triplets.
"""


class Solution:
    def countGoodTriplets(self, arr, a, b, c):
        count = 0
        n = len(arr)

        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                    for k in range(j + 1, n):

                        if ((a >= abs(arr[j] - arr[i])) and 
                            (b >= abs(arr[k] - arr[j])) and 
                            (c >= abs(arr[k] - arr[i]))):
                            
                            count += 1
                        
        return count
