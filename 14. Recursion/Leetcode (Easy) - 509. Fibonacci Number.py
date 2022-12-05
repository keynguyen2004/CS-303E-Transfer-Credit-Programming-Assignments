"""
Leetcode Problem #: 509
Leetcode Problem: Fibonacci Number
Difficulty: Easy

This is a common example of a problem that is best solved using recursion. 
We can start by defining our base case. This is our stop conditions. The 
bottom of the tower of recursive calls that we are building. 

Next we want to do our recursive case that is essentially spelt out in the 
problem statement. Here we are calling fib inside of fib. But each time we 
are reducing n and hence we will eventually hit our base case. For instance,
let's take fib(n) where n = 7

fib(7) = fib(6) + fib(5)
fib(7) = (fib(5) + fib(3)) + (fib(4) + fib(2))
fib(7) = ((fib(4) + fib(3)) + fib(2) + fib(1)) + ((fib(3) + fib(2)) + (fib(1) + fib(0)))
…

"""

class Solution:
    def fib(self, n):
        if n <= 1:
            return n
        return self.fib(n-1) + self.fib(n-2)

# However, we can optimize the solution by avoiding redundant recursion call using hashmap

class Solution:
    def fib(self, n, dic):
        if n <= 1:
            return n
        if n in dic:
            return dic[n]
        dic[n] = self.fib(n-1, dic) + self.fib(n-2, dic)
        return dic[n]

# Alternatively, this problem can be solve iteratively

class Solution:
    def fib(self, n) :
        if n <= 1:
            return n
        
        first = 0
        second = 1
        for i in range(2, n + 1):
            first, second = second, first + second
        return second