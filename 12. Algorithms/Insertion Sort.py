"""
Insertion sort follow these 5 steps

    1. Set the first element to be the sorted list  
    2. Store the next element in a temporary variable // 
       store the value to be sorted in a temporary variable 
    3. … compare this next element to each element in the sorted list  
    4. Move the elements that are greater/less than it one space to 
       the right and insert the temporary variable // swap the element 
       down until in the correct positions  
    5. Loop through all items from 2nd to end of array 

Assignments: 

    1. Exercise #1: Sort student information

"""

# Insertion sort in ascending order
def ascendingInsertionSort(numbers):
    for i in range (1, len(numbers)):
        currentNumber = numbers[i]
        comparedIndex = i - 1

        while (comparedIndex >= 0) and (numbers[comparedIndex] > currentNumber):
            numbers[comparedIndex + 1] = numbers[comparedIndex]
            comparedIndex -= 1
        numbers[comparedIndex + 1] = currentNumber
        
    print(numbers)
    
# Insertion sort in descending order
def descendingInsertionSort(numbers):
    for i in range (1, len(numbers)):
        currentNumber = numbers[i]
        comparedIndex = i - 1

        while (comparedIndex >= 0) and (numbers[comparedIndex] < currentNumber):
            numbers[comparedIndex + 1] = numbers[comparedIndex]
            comparedIndex -= 1
        numbers[comparedIndex + 1] = currentNumber
        
    print(numbers)


if __name__ == "__main__":
    numbers = [3,2,4,5,1,6,9,0,8,7]
    ascendingInsertionSort(numbers)
    descendingInsertionSort(numbers)



# Exercise #1: Sort student information

def sortStudentInformation(studentName, studentScore):
    for i in range(1, len(studentName)):
        score = studentScore[i]
        firstName = studentName[i][0]
        lastName = studentName[i][1]
        comparedIndex = i - 1

        while (comparedIndex >= 0) and (studentScore[comparedIndex - 1] < score):
            studentScore[comparedIndex] = studentScore[comparedIndex - 1]
            studentName[comparedIndex][0] = studentName[comparedIndex - 1][0]
            studentName[comparedIndex][1] = studentName[comparedIndex - 1][1]
            comparedIndex -= 1
        
        studentScore[comparedIndex] = score
        studentName[comparedIndex][0] = firstName
        studentName[comparedIndex][1] = lastName
