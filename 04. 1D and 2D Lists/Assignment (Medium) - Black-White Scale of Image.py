"""
Assignment: Black-white scale of image

You are given a black & white image in form of m * n pixel 
matrix grid.

    1. If pixel[i][j] = 0 then pixel is black
    2. If pixel[i][j] = 1 then pixel is white

Calculate black-white scale of image.
The black-white scale of a pixel[i][j] = (number of 1s in ith row + 
number of 1s in jth column) - (number of 0s in ith row + 
number of 0s in jth column)

For this problem, we need calculate the total number of 0s 
and 1s in each row and column using preifx array. With that, 
we can use nested for loops to iterate over all the pixels 
and check the black-white scale
"""


def getBlackWhiteScale(pixels):
    arr = []

    for i in range (len(pixels)):
        arr.append(list(map(int, pixels[i])))

    rowList = []
    for j in range (len(arr)):
        rowSum = sum(arr[j])
        rowList.append(rowSum)

    colList = []
    for k in range (len(arr[0])):
        colSum = 0
        for l in range (len(arr)):
            colSum += arr[l][k]
        colList.append(colSum)

    row = len(arr)
    col = len(arr[0])

    matrix = [[0] * col] * row
    res = float("-inf")
    for i in range (len(arr)):
        for j in range (len(arr[0])):
            horizontal = rowList[i]
            vertical = rowList[j]
            matrix[i][j] = ((vertical + horizontal) * 2) - (row + col)
            res = max(res, matrix[i][j])
    
    return res