# almostIncreasingSequence
# https://app.codesignal.com/arcade/intro/level-2/2mxbGwLzvkTCKAJMG

def leftToRight(sequence):
    removeOneElement = False
    ptr1 = 0
    ptr2 = 1
    while(ptr2 < len(sequence)):
        if (sequence[ptr1] >= sequence[ptr2]):
            if (removeOneElement == True):
                return False
            removeOneElement = True
            ptr2 += 1
        else:
            ptr1 = ptr2
            ptr2 += 1
    print ptr1, ptr2
    return True

def rightToLeft(sequence):
    removeOneElement = False
    ptr1 = len(sequence) -1
    ptr2 = ptr1 - 1
    while(ptr2 >= 0):
        if (sequence[ptr1] <= sequence[ptr2]):
            if (removeOneElement == True):
                return False
            removeOneElement = True
            ptr2 -= 1
        else:
            ptr1 = ptr2
            ptr2 -= 1
    print ptr1, ptr2
    return True

def solution(sequence):
    if (len(sequence) <= 2):
        True
    if leftToRight(sequence):
        return True
    print "hello we are here"
    if rightToLeft(sequence):
        return True
    print "hello we are here again"
    return False
