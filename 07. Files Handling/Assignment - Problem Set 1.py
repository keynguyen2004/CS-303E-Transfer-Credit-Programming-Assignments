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
    def displayLine(self):
        file = open("theatreScript.txt", "r")

        for line in file:
            if ((line.lower() != "break") and not 
                (line.startswith("Note"))):
                print(line)
        
        file.close()


if __name__ == "__main__":
    textFile = Solution()
    textFile.displayLine()



# Question 2

class Solution:
    def displayLineNumber(self):
        file = open("computerScienceGuide.txt", "r")
        count = 0 

        for line in file:
            if (("algorithm") in line.lower() or 
                ("data structure") in line.lower()):
                count += 1
        
        file.close()
        print(count)


if __name__ == "__main__":
    textFile = Solution()
    textFile.displayLineNumber()



# Question 3

class Solution:
    def totalLetterCount(self):
        file = open("medicalPrescription.txt", "r")
        letterCount = 0
        line = file.read()
        arr = line.split()

        for word in arr:
            for char in word:
                if not char.isdigit():
                    letterCount += 1

        file.close()
        print(letterCount)


    def totalEvenNumberCount(self):
        file = open("medicalPrescription.txt", "r")
        evenNumCount = 0
        line = file.read()
        arr = line.split()

        for word in arr:
            for char in word:
                if char.isdigit() and int(char)%2 == 0:
                    evenNumCount += 1

        file.close()
        print(evenNumCount)


if __name__ == "__main__":
    textFile = Solution()
    textFile.totalLetterCount()
    textFile.totalLetterCount()