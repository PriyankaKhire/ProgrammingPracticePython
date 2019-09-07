def findLeft(heights, k):
    current = k
    for height in range(k, -1, -1):
        print height, heights[height]
        if(heights[height] < heights[current]):
            current = height
        elif(heights[height] > heights[current]):
            break
    if(current == k):
        return False, -1
    return True, current

def findRight(heights, k):
    current = k
    for height in range(k, len(heights)):
        if(heights[height] < heights[current]):
            current = height
        elif(heights[height] > heights[current]):
            break
    if(current == k):
        return False, -1
    return True, current

def logic(heights, k, v):
    for water in range(v):
        # if there is left
        flag, index = findLeft(heights, k)
        if(flag):
            heights[index] = heights[index]+1
        else:
            flag, index = findRight(heights, k)
            if(flag):
                heights[index] = heights[index]+1
            else:
                heights[k] = heights[k]+1
    print heights

# Main
#logic([2,1,1,2,1,2,2], 3, 4)
logic([1,2,3,4,3,2,1,2,3,4,3,2,1], 5, 2)


