"""
Leetcode Problem #: 394
Leetcode Problem: Decode String 
Difficulty: Medium

We build the string recursively by always triggering a new call to the 
recursive method when '[' is detected, we return the index where the 
calling method should continue the parsing from, and the string that 
should be added to the full result. It is important to remember to reset 
the num variable when we get the return value from another call because 
there might a string such as 3[c]2[a].

"""

class Solution:
    def decodeString(self, s):
        def decode(s, index):
            num = currStr = ""
            while index < len(s):
                if str(s[index]).isnumeric():
                    num += s[index]
                elif s[index] == '[':
                    index, newStr = decode(s, index + 1)
                    for i in range(int(num) if num else 1):
                        currStr += newStr
                    num = ""
                    continue
                elif s[index] == ']':
                    return (index + 1, currStr)
                else:
                    currStr += s[index]
                index += 1
            return (index + 1, currStr)
        return decode(s, 0)[1]


# To illustrate the problem easier, we can solve this iteratively

class Solution:
    def decodeString(self, s):
        stack = []
        currStr, num = "", 0
        for char in s:
            if char == "[":
                stack.append(currStr)
                stack.append(num)
                currStr, num = "", 0
            elif char == "]":
                val = stack.pop()
                prevStr = stack.pop()
                currStr = prevStr + currStr * val
            elif char.isdigit():
                num = num*10 + int(char)
            else:
                currStr += char
        return currStr
