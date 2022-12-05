"""
open() function takes two parameters: filename and mode.
f = open("demofile.txt", "rt")


The 4 different modes for opening a file are

"r" - Read - Default value. Opens a file for reading, error if the file does not exist
"a" - Append - Opens a file for appending, creates the file if it does not exist
"w" - Write - Opens a file for writing, creates the file if it does not exist
"x" - Create - Creates the specified file, returns an error if the file exists


In addition you can specify if the file should be handled as binary or text mode

"t" - Text - Default value. Text mode
"b" - Binary - Binary mode (e.g. images)
"""



# Question 1

class Solution:
    def letterFrequency(self):
        file = open("farmerAlamanac.txt", "r")
        letter = {}
        line = file.read()
        arr = line.split()

        for word in arr:
            for char in word:
                if char in letter:
                    letter[char] += 1
                else:
                    letter[char] = 1

        file.close()
        res = []
        res = sorted(letter.items(), key = lambda x:-x[1])

        for letter, frequency in res:
            print(letter + " : " + str(frequency))


if __name__ == "__main__":
    textFile = Solution()
    textFile.letterFrequency()




# Question 2

class Solution:
    def minimumAdjacentSwaps(self):
        file = open("envelopeColor.txt", "r")
        minSwap = 0

        for line in file:
            arr = line.split()
            color = arr[-1]
            curSwap = self.swapCount(arr, color)
            minSwap = min(curSwap, minSwap)
            print("Color: ", color)
            print("Minimum adjacent swaps: ", minSwap)

        file.close()


    def swapCount(self, arr, color):
        count = 0
        end = 0
        for i in range (len(arr)):
            if arr[i] == color:
                count += i - end
                end += 1
            return count


if __name__ == "__main__":
    textFile = Solution()
    textFile.minimumAdjacentSwaps()



# Question 3

class Solution:
    def primeNumber(self, limit):
        file = open("primeNumber.txt", "w")
        if limit % 10 == 0:
            order = limit//10
        else:
            order = limit//10 + 1

        index = 1
        arr = self.getPrime(self, limit)

        if arr == [0]:
            return False

        while index <= order:
            for i in range (index):
                for index, val in enumerate(arr):
                    if ((val == 1) and (val < index*10)):
                        file.write(index, end = " ")
                    else:
                        file.write("\n")
                        break
            index += 1

        file.close()


    def getPrime(self, num):
        if num < 2:
            return [0]

        res = [0,0] + [1] * (num - 2)
        i = 2

        while i**2 <= num:
            if res[i]:
                res[i**2:num + 1:i] = [0] * ((((num + 1) - i**2
                                       - 1)//i) + 1)
            if i != 2:
                i += 2
            else:
                i += 1

        return res


if __name__ == "__main__":
    textFile = Solution()
    textFile.primeNumber()
        