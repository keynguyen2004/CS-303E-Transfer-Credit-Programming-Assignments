"""
Leetcode Problem #: 65
Leetcode Problem: Valid Number
Difficulty: Hard

For this problem, we need to be mindful of the constraints 
and corner cases. For instances

    1. There can be 0 or 1 sign in each number part if there 
       is a sign at the first index of the number part.
    2. 0 can have sign: "+0"
    3. There can be leading 0s: "00.000", "007"
    4. The first part of the decimal number can start with 
       dot .: ".8"

Therefore, we can utilize exception handling to get rid of the 
invalid corner cases
"""


# First solution

class Solution:
    def isNumber(self, s):

        invalidLeadingSign = ["++", "+-", "-+", "--"]

        if s[:2] in invalidLeadingSign:
            return False

        try:
            decimal = float(s)
        except ValueError:
            return False
        except SyntaxError:
            return False

        return True



# Second solution

class Solution:
    def isNumber(self, s):
        string = s.split()

        if len(string) > 1:
            return False

        try:
            integer = int(s)
        except ValueError:
            try:
                float(s)
                return True
            except ValueError:
                return False

        return True