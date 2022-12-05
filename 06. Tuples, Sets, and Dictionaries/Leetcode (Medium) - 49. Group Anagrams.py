"""
Leetcode Problem #: 49
Leetcode Problem: Group Anagrams
Difficulty: Medium

For this problem, we'll make use of dictionary to store the sorted
letters and an array containing the corresponding anagrams with the
same group of letters. 

Consider example 1 : strs = ["eat","tea","tan","ate","nat","bat"]
                
After the opeartion, the dictionary will contain

{
    "aet": [eat, tea, ate]
    "ant": [tan, nat]
    "abt": [bat]
}

"""

class Solution:
    def groupAnagrams(self, strs):
        if len(strs) == 1:
            return [strs]

        dic = {}
        for i in range (len(strs)):
            w = strs[i]
            sort = "".join(sorted(w))
            if sort not in dic:
                dic[sort] = [w]
            else:
                dic[sort].append(w)
        return dic.values()



# Alternatively, we can make use of the ASCII value of each letter

class Solution:
    
    def groupAnagrams(self, strs):

        from collections import defaultdict 

        def ascii(string):
            digit, power = 0, 1
            asciiDif = ord('z') - ord('a')

            for char in sorted(string):
                digit += power * (ord(char) - ord('a'))
                power *= asciiDif
            return digit

        dic = defaultdict(lambda: [])
        for w in strs:
            dic[ascii(w)].append(w)
        return dic.values()
