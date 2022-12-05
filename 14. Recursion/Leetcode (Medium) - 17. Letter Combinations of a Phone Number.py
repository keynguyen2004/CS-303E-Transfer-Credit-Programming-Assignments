"""
Leetcode Problem #: 17
Leetcode Problem: Letter Combinations of a Phone Number
Difficulty: Medium

For this particular problem, we can approach this iteratively where we switch
the corresponding letters for each number.
"""

class Solution:
    def letterCombinations(self, digits):

        if not digits:
            return []

        dic = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        n = 1

        for num in digits:
            n *= len(dic[num])
        
        res = [""] * n
        switch = n

        for num in digits:
            length = len(dic[num])
            switch //= length
            arr = [char for char in dic[num]]
            i, j = 0, 0
            while i < n:
                res[i] += arr[j]
                i += 1
                if i % switch == 0:
                    if j == length - 1:
                        j = 0
                    else:
                        j += 1
        return res
        
    
# From this iterative solution, we can implement a similar recursive approach

class Solution:
    def letterCombinations(self, digits):
        
        if not digits:
            return []

        dic = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        res = []

        def recursion(res, dic, digits, index, cur):
            if index >= len(digits):
                res.append(cur)
                return 
                
            letters = dic[digits[index]]

            for letter in letters:
                    recursion(res, dic, digits, index + 1, cur + letter)
        
        recursion(res, dic, digits, 0, '')
        
        return res    