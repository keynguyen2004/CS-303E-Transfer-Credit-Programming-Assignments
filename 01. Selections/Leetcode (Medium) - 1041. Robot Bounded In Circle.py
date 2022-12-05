"""
Leetcode Problem #: 1041
Leetcode Problem: Robot Bounded In Circle
Difficulty: Medium

The rectangular components of the current unit vector which represents 
the direction in which robot is facing. Once all the instructions are 
executed, if the final state of the vector is not equal to its initial 
state or the robot comes back at (0,0) then the robot wil remain bounded
in a circle.

"""

class Solution:
    def isRobotBounded(self, instructions):
        x, y, switch = 0
        leftDirection = [(0,1), (-1,0), (0,-1), (1,0)]
        rightDirection = [(0,1),(1,0),(0,-1),(-1,0)]
        movement = ["left", 0]

        for i in range (4):
            for instruction in instructions:
                if instruction != "G":
                    
                    if instruction == "R":
                        movement[0] = "right" 
                    else:
                        movement[0] = "left"

                    if ((movement[0] == "left" and instruction == "R") or 
                    (movement[0] == "right" and instruction == "L")):
                        switch += 1 

                    if switch % 2 == 1:                    
                        if movement[1] <= 0:
                            movement[1] = 3
                        else:
                            movement[1] -= 1
                    else:
                        if movement[1] >= 3:
                            movement[1] = 0
                        else:
                            movement[1] += 1
                              
                else:
                    if movement[0] == "right":
                        x += rightDirection[movement[1]][0]
                        y += rightDirection[movement[1]][1]
                    else:
                        x += leftDirection[movement[1]][0]
                        y += leftDirection[movement[1]][1]
                    
            if ((movement[1] == 0 or movement[1] == 2) and (x == 0) and (y == 0)):
                return True

        return False
                        