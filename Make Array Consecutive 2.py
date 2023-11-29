# Make Array Consecutive 2
# https://app.codesignal.com/arcade/intro/level-2/bq2XnSr5kbHqpHGJC

def solution(statues):
    if (len(statues) <= 1):
        return 0
    sortedHeights = sorted(statues)
    # count the number of statues needed
    count = 0
    for i in range(len(statues)-1):
        currNum = sortedHeights[i]
        while(currNum+1 != sortedHeights[i+1]):
            count += 1
            currNum += 1
    return count
