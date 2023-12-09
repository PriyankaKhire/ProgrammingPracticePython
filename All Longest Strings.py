# All Longest Strings
# https://app.codesignal.com/arcade/intro/level-3/fzsCQGYbxaEcTr2bL
def solution(inputArray):
    # key = length value = [list of words of that length]
    hashtable = {}
    for string in inputArray:
        if not len(string) in hashtable:
            hashtable[len(string)] = []
        hashtable[len(string)].append(string)
    return hashtable[max(hashtable)]
