"""
The binary search only works for an ordered list - either ascending or descending. 
It calculates the midpoint index and checks the value at this position.

    1. If the value at the midpoint index is the target value, the algorithm ends.
    2. If the value at the midpoint index is less than the target value, adjust the 
       midpoint index so that it neglect all the items before the item at the midpoint
       index (inclusive). In other words, midpoint = low + 1
    3. If the value at the midpoint index is greater than the target value, adjust the 
       midpoint index so that it neglect all the items after the item at the midpoint
       index (inclusive). In other words, midpoint = high - 1

The binary search can be done either iteratively or recursively
"""

# Iterative binary search
def binarySearch(numbers, target):
    low = 0
    high = len(numbers) - 1
    flag = False

    while low <= high and flag == False:
        mid = (low + high)//2
        if numbers[mid] == target:
            print("Found the target value at index", mid)
            flag = True
        elif numbers[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    
    if flag == False:
        print("The array doesn't contains the target value")

if __name__ == "__main__":
    numbers = [0,1,2,3,4,5,6,7,8,9]
    binarySearch(numbers, 3)
    binarySearch(numbers, 10)


# Recursive binary search

def binarySearch(numbers, target, low, high):
    if low <= high:
        mid = (low + high)//2
        if numbers[mid] == target:
            return "Found the target value at index " + str(mid)
        elif numbers[mid] < target:
            return binarySearch(numbers, target, mid + 1, high)
        else:
            return binarySearch(numbers, target, low, mid - 1)
    else:
        return "The array doesn't contains the target value"

if __name__ == "__main__":
    numbers = [0,1,2,3,4,5,6,7,8,9]
    low = 0
    high = len(numbers) - 1
    print(binarySearch(numbers, 3, low, high))
    print(binarySearch(numbers, 10, low, high))  