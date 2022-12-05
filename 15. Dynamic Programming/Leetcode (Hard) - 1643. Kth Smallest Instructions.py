"""
Leetcode Problem #: 1643
Leetcode Problem: Kth Smallest Instructions 
Difficulty: Hard

There are two choices at each index, go with "H" or go with "V". 
The one to choose can be determined by k.

There are nCr(i+j, j) bitstrings can you make with i 0's and j 1's. You have i + j steps 
and j of them must be 1's. Out of all these bitstrings, there are nCr(i+j-1,j) of them 
start with 0. You set the first bit as 0, and you are left with i+j-1 bits remaining to 
assign, j of them must be ones. Therefore, there are nCr(i+j-1,j-1) bitstrings start with
1. So, i+j-1 bits left to assign, j-1 of them must be 1.

The recursion is: If k <= nCr(i+j-1,j-1), then our answer must start with "H". Then, we 
assign the rest of the bits and make the recursive call. If k > nCr(i+j-1,j-1), then the 
answer must start with "V", and we subtract nCr(i+1-1,j-1) from k and make the recursive 
call.The strings that start with "H" are lexicographically smaller than the strings that 
start with "V".

The base case is k = 1, which we can assign the lexicographically smallest string using 
all "H"'s first then using all "V"'s.
"""

class Solution:

    def kthSmallestPath(self, destination, k):
        from math import comb

        i, j = destination
        
        def instruction(i, j, k):
            if k == 1:
                return ("H" * j) + ("V" * i)
            else:
                totalCombination = comb(i+j-1, j-1)
                if k <= totalCombination:
                    return "H" + instruction(i, j-1, k)
                else:
                    return "V" + instruction(i-1 ,j , k-totalCombination)
        
        return instruction(i, j, k)


    # Similarly, we can implement the solution using iteration.

    def kthSmallestPath(self, destination, k):
        from math import comb

        path = ""
        i, j = destination

        remainingRow = i
        for instructions in range (i + j):
            remainingStep = i + j - (instructions + 1)
            totalCombination = comb(remainingStep, remainingRow)
            if k <= totalCombination:
                path += "H"
            else:
                remainingRow -= 1
                k -= totalCombination
                path += "V"
        return path

