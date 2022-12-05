"""
Leetcode Problem #: 893
Leetcode Problem: Groups of Special-Equivalent Strings
Difficulty: Medium

For this particular problem, we will approach it with the following steps

    1. We maintain 2 arrays of length 26 (since there're 26 letters in alphabet): 
       one for odd positions and one for even positions.
    2. The value of the indexed character is incremented if its repeated in the word.
    3. Once the operation is finished, we generate an encoded string by taking 
       the value of each index of both the arrays and placing it side by side. 
       
Note: We will maintain hash set so that it will ignore duplicate words

"""

class specialEquivalent:
    def __init__(self, word):

        self.arr1 = [0] * 26
        self.arr2 = [0] * 26

        for char in word[0:len(word):2]:
            self.arr2[ord(char) - ord('a')] += 1

        for char in word[1:len(word):2]:
            self.arr1[ord(char) - ord('a')] += 1
        

    def __equalizer__(self, string):
        return self.arr1 == string.arr1 and self.arr2 == string.arr2 

    def __hashing__(self):
        return hash(str(self.arr1 + self.arr2))
    
class Solution:
    def numSpecialEquivGroups(self, words):
        string = set(specialEquivalent(s) for s in words)
        return len(string)


# We can shorten the solution by reducing the number of function 
# (i.e. remove class specialEquivalent)

class Solution:
    def numSpecialEquivGroups(self, words):
        string = set()
        for s in words:
            arr1 = list(sorted(s[0:len(s):2]))
            arr2 = list(sorted(s[1:len(s):2]))
            string.add(arr1, arr2)

        return len(string)