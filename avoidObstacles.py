# avoidObstacles
# https://app.codesignal.com/arcade/intro/level-5/XC9Q2DhRRKQrfLhb5
'''
You are given an array of integers representing coordinates of obstacles situated on a straight line.
Assume that you are jumping from the point with coordinate 0 to the right. You are allowed only to make jumps of the same length represented by some integer.
Find the minimal length of the jump enough to avoid all the obstacles

Better explanation:
We are given coordinates of obstacles on a straight line. We start jumping from point 0, we need to reach the end, avoiding all obstacles. 
The length of every jump has to be the same (For example, if we jump from 0 to 4, then we must make the next jump from 4 to 8). 
We need to find the minimum length of the jump so that we can reach the end and we avoid all obstacles.
'''

def solution(inputArray):
    # sort the array
    inputArray.sort()
    # We can check if the array is consecutive or not but that will only improve the average time complexity
    # The time complexity of this solution is O(n)
    maxNum = inputArray[-1]
    jumpLength = 1
    coordinate = 0
    while (coordinate <= maxNum):
        if (coordinate+jumpLength in inputArray):
            # start from beginning and increase the jump length by one
            coordinate = 0
            jumpLength += 1
        else:
            coordinate += jumpLength
    return jumpLength
