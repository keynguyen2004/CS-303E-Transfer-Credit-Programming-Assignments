"""
Leetcode Problem #: 242
Leetcode Problem: Valid Anagram
Difficulty: Easy

Anagrams are those strings in which character and frequency
of those character are same. We can observe that the characters 
stay the same, and the amount of time they occur in the string 
stays the same.

Thefore, we are going to count how many times the characters occur
in s and check whether the same characters occur the same amount of
times in t. We will store the character count using a dictionary.
"""

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        dic = {}
        for i in range (len(s)):
            if s[i] in dic:
                dic[s[i]] += 1
            else:
                dic[s[i]] = 1

        for i in range(len(t)):
            if t[i] in dic:
                dic[t[i]] -= 1
            else:
                return False

        return all(val == 0 for val in dic.values())


# Alternatively, we can make use of the ASCII value of each letter

class Solution:
    def isAnagram(self, s, t):

        if len(s) != len(t):
            return False

        arr = [0] * 26

        for i in range(len(s)):
            arr[ord(t[i]) - ord('a')] -= 1
            arr[ord(s[i]) - ord('a')] += 1

        for j in range(len(arr)):
            if arr[j] != 0:
                return False

        return True