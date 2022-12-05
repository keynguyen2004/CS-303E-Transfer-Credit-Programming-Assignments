"""
Leetcode Problem #: 500
Leetcode Problem: Keyboard Row
Difficulty: Easy

For this problem, we loop through every word in the array and
set a counter to be reset when moving on to the next word. When
loop through every character in the current word, if the current
word is in the first/second/third and every character is from the
same row, add the result to the array
"""

class Solution:
    def findWords(self, words):
        one, two, three = set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")
        sets = [one, two, three]
        
        res = []
        
        for w in words:
            row = 0
            flag = True
            
            if w[0] in sets[0]:
                row = 0
            elif w[0] in sets[1]:
                row = 1
            elif w[0] in sets[2]:
                row = 2
            
            for c in w:
                if c not in sets[row]:
                    flag = False
                    
            if flag == True:
                res.append(w)
            
        return res



# For the purpose of concision, we can shorten our solution

class Solution:
    def findWords(self, words):
        res = []
        sets = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        for w in words:
            for subset in sets:
                if set(w.lower()).issubset(subset):
                    res.append(w)
        return res