# Box Blur
# https://app.codesignal.com/arcade/intro/level-5/5xPitc3yT3dqS7XkP
'''
Last night you partied a little too hard. Now there's a black and white photo of you that's about to go viral! You can't let this ruin your reputation, so you want to apply the box blur algorithm to the photo to hide its content.
The pixels in the input image are represented as integers. The algorithm distorts the input image in the following way: Every pixel x in the output image has a value equal to the average value of the pixel values from the 3 × 3 square that has its center at x, including x itself. All the pixels on the border of x are then removed.
Return the blurred image as an integer, with the fractions rounded down.

Example

For

image = [[1, 1, 1], 
         [1, 7, 1], 
         [1, 1, 1]]
the output should be solution(image) = [[1]].

To get the value of the middle pixel in the input 3 × 3 square: (1 + 1 + 1 + 1 + 7 + 1 + 1 + 1 + 1) = 15 / 9 = 1.66666 = 1. The border pixels are cropped from the final result.
'''
def getAvg(matrix, midRow, midCol):
    topRowSum = matrix[midRow-1][midCol-1] + matrix[midRow-1][midCol] + matrix[midRow-1][midCol+1]
    midRowSum = matrix[midRow][midCol-1] + matrix[midRow][midCol] + matrix[midRow][midCol+1]
    bottomRowSum = matrix[midRow+1][midCol-1] + matrix[midRow+1][midCol] + matrix[midRow+1][midCol+1]
    return (topRowSum+midRowSum+bottomRowSum)/9
    
def solution(image):
    output = []
    for row in range(1, len(image)-1):
        rowOutput = []
        for col in range(1, len(image[0])-1):
            rowOutput.append(getAvg(image, row, col))
        output.append(rowOutput)
    return output
