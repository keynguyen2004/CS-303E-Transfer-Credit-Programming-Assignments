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
    def emptyLine(self):
        file = open("incompleteNumber.txt", "r")
        count = 0
        empty = []

        for line in file:
            if line.strip():
                empty.append(count)
            count += 1

        file.close()

        arr = [1] * count
        for num in empty:
            arr[num] = 0

        file = open("incompleteNumber.txt", "a")
        for index, line in enumerate(arr):
            if line == 0:
                file.append("Line " + str(index + 1) + " is empty.")
            else:
                file.append("Line " + str(index + 1) + " is not empty.")

        file.close()


if __name__ == "__main__":
    textFile = Solution()
    textFile.emptyLine()



# Question 2

class Solution:
    def priorityLine(self):
        file = open("medicalPrescription.txt", "r+")
        line = file.read()
        arr = line.split()

        start = -1
        end = 0
        indexPrior = 0
        startVal = arr[0]
        up = set()

        for index, word in enumerate(arr):

            if word == startVal:
                start = index
                indexPrior = index
                up = set()
                file.write("1")
            elif word in up:
                file.write("0")
            elif word == arr[indexPrior]:
                up.add(arr[indexPrior])

                if indexPrior == len(arr) - 1:
                    end = index
                    break
                indexPrior += 1

        file.close()

        if end == 0:
            print(-1)
        else:
            print(start - end + 1)


if __name__ == "__main__":
    textFile = Solution()
    textFile.priorityLine()