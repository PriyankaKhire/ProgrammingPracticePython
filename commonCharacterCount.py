# commonCharacterCount
# https://app.codesignal.com/arcade/intro/level-3/JKKuHJknZNj4YGL32
def solution(s1, s2):
    # key = character val = count
    hashTable = {}
    # Get count of char in string 1
    for char in s1:
        if not char in hashTable:
            hashTable[char] = 0
        hashTable[char] += 1
    commonChar = 0
    # compare characters from string 2 with characters of string 1
    for char in s2:
        if not char in hashTable:
            continue
        # if character found in hash table then we see if the count of character is greater than 0
        if (hashTable[char] > 0):
            commonChar += 1
            hashTable[char] -= 1
    return commonChar

