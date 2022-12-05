"""
Assignment #1: Group Connection

For a given matrix representation, matrix[i][j] = 1 means
person i and person j knows each other and thus, share a 
connection. For instance matrix[0][1] = 1 means person 0 
and person 1 knows each other, forming a group connection.

Find the group number.
"""

class Solution:
    def groupConnection(self, matrix):

        def dfs(index, row, matrix):
            if matrix[index][index] == 0:
                return

            for j in range (row):
                if matrix[index][j] == 1:
                    matrix[index][j] = 0
                    dfs(j, row, matrix)
        
        def stringToArr(string):
            res = []

            for word in string:
                res.append([int(num) for num in word])
            return res

        group, row = 0, len(matrix)
        matrix = stringToArr(matrix)

        for index in range (row):
            if matrix[index][index] == 1:
                group += 1
                dfs (index, row, matrix)

        return group



"""
Assignment #2: Binary-Denary Conversion

Create two functions which convert binary number into 
denary number and vice versa.

For example, 01101 is equals to 13
"""

class Solution:
    def binaryToDenary(self, binary):
        denaryNum, pow = 0
        binary = int(binary)

        while binary != 0:
            rem = binary%10
            binary = binary//10
            denaryNum += rem*(2**pow)
            pow += 1

        return denaryNum


    def denaryToBinary(self, denary):
        binaryNum, pow = 0

        while denary != 0:
            rem = denary%2
            denary = denary//2
            binaryNum += rem * pow
            pow *= 10

        return binaryNum