
def isPalindrome(word):
    for i in range(len(word)/2):
        if(word[i] != word[len(word)-1-i]):
            return False
    return True

def reverseWords(words):
    res = []
    for word in words:
        res.append(word[::-1])
    return res

def compareWords(w1, w2):
    i = 0
    j = 0
    while(i < len(w1) and j < len(w2)):
        if(w1[i] != w2[j]):
            # stop if no matching letters
            return False
        i = i+1
        j = j+1
    # if you reached here that means the longer words remaining letters need to be a palindrome
    if(len(w1) > len(w2)):
        return isPalindrome(w1[i:])
    return isPalindrome(w2[j:])

def emptyString(w1, w2):
    if(w1 == ""):
        return isPalindrome(w2)
    return isPalindrome(w1)

def main(words):
    rWords = reverseWords(words)
    for i in range(len(words)):
        for j in range(len(words)):
            if(i == j):
                continue
            #print words[i], words[j]
            #3) is either is empty string
            if(words[i] == "" or words[j] == ""):
                if(emptyString(words[i], words[j])):
                    print i, j
                continue
            #1) if both words are equal the yes add to result
            if(words[i] == rWords[j]):
                print i, j
                continue
            # 2) if both words dont start from same letter then continue
            if(words[i][0] != rWords[j][0]):
                continue
            if(compareWords(words[i], rWords[j])):
                print i,j
    
# Main
words = ["abcd","dcba","lls","s","sssll"]
main(words)

words = ["bat","tab","cat"]
main(words)

words = ["a",""]
main(words)

words = ["a","abc","aba",""]
main(words)

print "Reverse the words in given list and store them"
print "Start the comparision"
print "1) if equal then add to result\n\n"
print "2) compare the first letter of every string to the reversed string"
print "i) stop if no match after few letters"
print "ii) if all letters match then send the longer word to isPalindrome, we need rest of its letters to be palindrome\n\n"
print "3) if one string is empty then check if other stirng is palindrome or not"
