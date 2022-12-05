"""
Leetcode Problem #: 1291
Leetcode Problem: Sequential Digits
Difficulty: Medium

To begin with, I did the brute force approach of trying all
of 36 combinations of sequential numbers. However, to optimize 
the solution, and in case the range of the constaints is greater
(e.g. for alphabetical letters), we will need 2 for loops to add 
the digits. Every time slide the windown, check whether the number 
is in range of the low-high limit.
"""

# Brute force solution
class Solution:
    def sequentialDigits(self, low, high):
        
        res = []
        sequence = [
            12, 23, 34, 45, 56, 67, 78, 89,
            123, 234, 345, 456, 567, 678, 789,
            1234, 2345, 3456, 4567, 5678, 6789,
            12345, 23456, 34567, 45678, 56789,
            123456, 234567, 345678, 456789,
            1234567, 2345678, 3456789,
            12345678, 23456789,
            123456789
        ]

        for num in sequence:
            if low <= num <= high:
                res.append(num)

        return res


# Sliding window solution
class Solution:
    def sequentialDigits(self, low, high):

        res = []
        sequennce = "123456789"
        lower, upper = len(str(low)), len(str(high))

        for i in range (lower, upper + 1):
            for j in range (10-i):
                num = int(sequennce[j: j + i])
                if low <= num <= high:
                    res.append(num)
        return res