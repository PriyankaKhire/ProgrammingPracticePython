# centuryFromYear
# https://app.codesignal.com/arcade/intro/level-1/egbueTZRRL5Mm4TXN

def solution(year):
    if (year%100 == 0):
        return year/100
    return (year/100) + 1
