# palindromeRearranging
# https://app.codesignal.com/arcade/intro/level-4/Xfeo7r9SBSpo3Wico
'''
Given a string, find out if its characters can be rearranged to form a palindrome.

Example

For inputString = "aabb", the output should be
solution(inputString) = true.

We can rearrange "aabb" to make "abba", which is a palindrome.
'''

def countChar(inputString):
    hashMap = {}
    for char in inputString:
        if (char not in hashMap):
            hashMap[char] = 0
        hashMap[char] += 1
    return hashMap

def evenStringCharCount(hashMap):
    for key in hashMap:
        if (hashMap[key]%2 == 1):
            return False
    return True

def oddStringCharCount(hashMap):
    oddCharCount = 0
    for key in hashMap:
        if (hashMap[key]%2 == 1):
            oddCharCount += 1
    if (oddCharCount > 1):
        return False
    return True
    
def solution(inputString):
    # for a stirng to be a palindrome, it needs to have even numbers of each of the letters
    # if the string has odd number of characters then one character can have odd number of letters
    hashMap = countChar(inputString)
    if (len(inputString)%2 == 0):
        return evenStringCharCount(hashMap)
    else:
        return oddStringCharCount(hashMap)
