# shapeArea
# https://app.codesignal.com/arcade/intro/level-2/yuGuHvcCaFCKk56rJ

def getMiddleRowNumber(n):
    prevSquares = 1
    for i in range(2, n+1):
        prevSquares += 2
    return prevSquares

def getSideSquares(currRowSquares, totalSquaresOnCurrSide):
    print currRowSquares, totalSquaresOnCurrSide
    if (currRowSquares == 1):
        return
    # just remove 2 squares every time
    totalSquaresOnCurrSide[0] += currRowSquares - 2
    getSideSquares(currRowSquares-2, totalSquaresOnCurrSide)
    
        
def solution(n):
    if (n == 1):
        return 1
    # get number of squares in middle row.
    middleRowSquares = getMiddleRowNumber(n)
    # get number of squares on 1 side
    totalSquaresOnCurrSide = [0]
    getSideSquares(middleRowSquares, totalSquaresOnCurrSide)
    return middleRowSquares + (totalSquaresOnCurrSide[0] * 2)
    
    


