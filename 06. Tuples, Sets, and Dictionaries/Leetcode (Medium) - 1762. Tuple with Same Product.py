"""
Leetcode Problem #: 1762
Leetcode Problem: Tuple with Saem Product
Difficulty: Medium

For this problem, we can count the number of pairs with 
equal product, each pair will be "expanded" to 8 tuples 
in the output. For each pair, there are (nC2) * 8 number
of possibilities

"""

def tupleSameProduct(nums):
    n = len(nums)
    res = []

    for i in range(n):
        for j in range(i + 1, n):
            res.append(nums[i] * nums[j])

    # Sort the array
    m = len(res)
    res.sort()

    frequency = []
    cur = res[0]
    total = 1
    for i in range(m):
        if res[i] != res[i - 1]:
            frequency.append(total)
            total = 1
            cur = res[i]
        else:
            if i > 0:
                total += 1
        
    ans = 0
    freq = len(frequency)
    for i in range (freq):
        ans += frequency[i] * ((frequency[i] - 1)//2)

    return 8 * ans



# Alternatively, we can shorten our solution using built-in functions

from math import comb
from collections import Counter
from itertools import combinations

class Solution:
    def tupleSameProduct(self, nums):
        dic = Counter()
        for i, j in combinations(nums, 2):
            dic[i * j] += 1

        ans = 0
        for val in dic.values():
            ans += comb(2, val)

        return 8 * ans