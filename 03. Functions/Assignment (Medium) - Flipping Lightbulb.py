"""
Assignment: Flipping lightbulb

A room is lit by ightbulbs arranged in a row. he lightbulbs can
be in 2 states: on (represented by a 1) or off (represented by a 
0). At each position of the lighbulb, the bulb at that particular
position is a multiple of the prime factors of the chosen number.
For each iteration, the lightbulb is flipped - its state changed. 

Determine whether the bulb is on or off after the iteration is done.
"""

class Solution:

    def bulb(self, state, visited):
        num = max(max(visited), len(state))
        traverse = self.bulbTraversal(self, num)
        bulbSet = set()

        for visit in visited:
            for flip in self.bulbState(visit, traverse):

                if flip not in bulbSet:
                    bulbSet.add(flip)
                else:
                    bulbSet.remove(flip)

        for i in range (len(state)):
            index = i + 1
            bulbList = self.bulbState(index, traverse)

            for flipped in bulbList:
                if flipped in bulbSet:
                    state[i] = 1 if state[i] == 0 else 0
            
            return state


    def bulbTraversal(self, num):
        res = set(i for i in range(2, num + 1))
        i = 2

        while i**2 < num:
            square = i**2
            while square <= num:
                if square in res:
                    res.remove(square)
                square += i
            if i == 2:
                i += 1
            else:
                i += 2

        return res
            

    def bulbState(self, num, arr):
        import math
        res = set()

        for i in range (1, round(math.sqrt(num)) + 1):
            if num%i == 0:
                for state in range(i, num//i):
                    if state in arr:
                        res.add(state)

            return res