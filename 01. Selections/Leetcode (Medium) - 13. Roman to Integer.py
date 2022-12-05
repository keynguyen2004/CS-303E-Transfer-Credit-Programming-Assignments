"""
Leetcode Problem #: 12
Leetcode Problem: Integer to Roman
Difficulty: Easy

At each position, the roman numeral follows the same pattern as illustrated 
below with the branch statements. The only change is what character represents 
1, 5 and 10, which depends on the units if they are 1s, 10s, 100s or 1000s.
"""

class Solution:
    def intToRoman(self, num):
        dic = {1000: "M", 500: "D", 100: "C", 50: "L", 10: "X", 5: "V", 1: "I"}
        roman = ""
        order = 1000

        while order >= 1:

            val = num//order
            if 0 < val <= 4:
                if val == 4:
                    roman += dic[order] + dic[5 * order]
                else:
                    roman += dic[order] * val
            elif val > 4:
                if val == 9:
                    roman += dic[order] + dic[10 * order]
                else:
                    roman += dic[5 * order] + (dic[order] * (val - 5))
            
            if val > 0:
                num %= order
            order = int(order/10)

        return roman



"""
Leetcode Problem #: 13
Leetcode Problem: Roman to Integer
Difficulty: Medium

We apply the same principle as the above problem, with only a slight tweak
in that we are now converting roman numeral to integer.
"""

class Solution:
    def romanToInt(self, s):
        dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        num = dic[s[0]]
        for i in range (1, len(s)):
            if (s[i] == "V" or s[i] == "X") and (s[i-1]) == "I":
                num += dic[s[i]] - 2
            elif (s[i] == "L" or s[i] == "C") and (s[i-1]) == "X":
                num += dic[s[i]] - 20
            elif (s[i] == "D" or s[i] == "M") and (s[i-1]) == "C":
                num += dic[s[i]] - 200
            else:
                num += dic[s[i]]
        return num