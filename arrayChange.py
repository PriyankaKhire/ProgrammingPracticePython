# arrayChange
# https://app.codesignal.com/arcade/intro/level-4/xvkRbxYkdHdHNCKjg
'''
You are given an array of integers. On each move you are allowed to increase exactly one of its element by one. Find the minimal number of moves required to obtain a strictly increasing sequence from the input.

Example

For inputArray = [1, 1, 1], the output should be
the strictly increasing sequence would be [1,2,3]
so we need to add 1 to element at index 1 and 2 to element at index 2 to get this answer
solution(inputArray) = 3.
'''
def solution(inputArray):
    moves = 0
    for i in range(1, len(inputArray)):
        # if the previous element is less than the current element
        if (inputArray[i-1] >= inputArray[i]):
            # get the difference between the 2 and add one to make it increasing
            currentMoves = (inputArray[i-1] - inputArray[i])+1
            # add the current moves to your previously counted moves
            moves += currentMoves
            # update the current element so now when we compare the next element we are comparing it against newly updated element
            inputArray[i] += currentMoves
    return moves
