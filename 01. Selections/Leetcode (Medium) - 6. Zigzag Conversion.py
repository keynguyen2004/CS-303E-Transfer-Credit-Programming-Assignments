"""
Leetcode Problem #: 6
Leetcode Problem: Zigzag Conversion
Difficulty: Medium

For the string s, we traverse it linearally. We keep track of its
oscillating period, and from that, locate the index of the character
in the string.
"""

class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        loop = 0  
        first = 1
        count = 1
        forward = True
        zigzag = s[0]

        for char in s[1:]:

            if count == numRows - 1:
                zigzag += char
                loop += 1
                forward = False

            elif count == 0:
                zigzag = zigzag[:first] + char + zigzag[first:]
                loop += 1
                first += 1
                forward = True

            else:
                if forward:
                    val = first + (count * loop) + count - 1
                else:
                    val = first + (count * (loop - 1)) + count
                zigzag = zigzag[:val] + char + zigzag[val:]


            if forward == True:
                count += 1
            else:
                count -= 1
            
        return zigzag



# To shorten our code so that it's more readable, we can use a 1D 
# array to store the index of the zigzag characters and another 1D
# array to zigzag characters themselves


class Solution:
    def convert(self, s, numRows):
        index = list(range(numRows)) + list(range(numRows - 2, 0, -1))
        n = len(index)

        res = [""] * numRows
        for i in range(len(s)):
            # Index of zigzag characters
            zigzagIndex = i % n

            # The oscillating index
            oscillatingIndex = index[zigzagIndex]

            # Store the zigzag characters themselves
            res[oscillatingIndex] += s[i]

        return "".join(res)
