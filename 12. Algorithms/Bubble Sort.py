"""
Bubble sort repeatedly compare consecutive pairs of value and 

    1. If the pair of value is in the wrong order, swap the value pair 
       and move onto the next pair
    2. If the pair of value is in the correct order, move onto the next pair

"""

# Bubble sort in ascending order
def ascendingBubbleSort(numbers):
    # An array of length n require n-1 sort operation
    for outerSwap in range (len(numbers) - 1):
        # An array of n elements required n-1 elements compared & swapped
        for innerSwap in range(len(numbers) - 1):
            if numbers[innerSwap] > numbers[innerSwap + 1]:
                temp = numbers[innerSwap]
                numbers[innerSwap] = numbers[innerSwap + 1]
                numbers[innerSwap + 1] = temp
    print(numbers)

# Bubble sort in descending order
def descendingBubbleSort(numbers):
    # An array of length n require n-1 sort operation
    for outerSwap in range (len(numbers) - 1):
        # An array of n elements required n-1 elements compared and swapped
        for innerSwap in range(len(numbers) - 1):
            if numbers[innerSwap] < numbers[innerSwap + 1]:
                temp = numbers[innerSwap]
                numbers[innerSwap] = numbers[innerSwap + 1]
                numbers[innerSwap + 1] = temp
    print(numbers)

if __name__ == "__main__":
    numbers = [3,2,4,5,1,6,9,0,8,7]
    ascendingBubbleSort(numbers)
    descendingBubbleSort(numbers)



# However, the solution can be inefficient as the array might be sorted already 
# but the compare & swap operations are still carrying on. We can reduce the number 
# of items to be checked by one after each pass and use of a flag to indicate if
# any swaps have taken place. Then, use a flag variable to stop the outer loop after 
# no more swaps made on a single pass of the inner loop, and set the flag accordingly 


# Bubble sort in ascending order
def ascendingBubbleSor(numbers):
    noSwap = False
    outerSwap = 0
    innerSwap = len(numbers) - 1

    while noSwap == False and outerSwap < len(numbers):
        noSwap = True
        for i in range (innerSwap):
            if numbers[i] > numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                noSwap = False
        innerSwap -= 1
    
    print(numbers)


# Bubble sort in descending order
def descendingBubbleSor(numbers):
    noSwap = False
    outerSwap = 0
    innerSwap = len(numbers) - 1

    while noSwap == False and outerSwap < len(numbers):
        noSwap = True
        for i in range (innerSwap):
            if numbers[i] < numbers[i + 1]:
                temp = numbers[i]
                numbers[i] = numbers[i + 1]
                numbers[i + 1] = temp
                noSwap = False
        innerSwap -= 1
    
    print(numbers)

if __name__ == "__main__":
    numbers = [3,2,4,5,1,6,9,0,8,7]
    ascendingBubbleSort(numbers)
    descendingBubbleSort(numbers)