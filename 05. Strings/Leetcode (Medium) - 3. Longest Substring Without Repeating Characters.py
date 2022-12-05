"""
Leetcode Problem #: 8
Leetcode Problem: String to Integer (atoi)
Difficulty: Medium

For this problem, we can use sliding window where sliding 
window (i, j) and maintain the occurrence count for each 
character in between.Then, We can expand it to right as 
long as the new character is not a duplicate. If it is a 
duplicate, we shrink the left side until we encounter the 
same character that can reduce our count to 1. 


"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        if len(s) == 0:
            return 0
        elif len(s) == 1:
            return 1
        else:
            char = [s[0]]
            countArr = [1]
            for i in range (1, len(s)):
                if s[i] not in char:
                    char.append(s[i])
                else:
                    countArr.append(len(char))
                    if char[len(char)-1] == s[i]:
                        char = [s[i]]
                    else:
                        index = 0
                        while True: 
                            if char[index] == s[i]:
                                char.remove(char[index])
                                break
                            char.remove(char[index])
                        char.append(s[i])
            countArr.append(len(char))
            return max(countArr)
            