#Print all palindromic partitions of a string
#http://www.geeksforgeeks.org/print-palindromic-partitions-string/

def isPalindrome(string):
    if len(string) == 1:
        return True
    for i in range(len(string)):
        if(string[i] != string[len(string)-1-i]):
            return False
    return True

def foo(string):
    result = []
    for start_i in range(len(string)):
        for end_i in range(start_i+1, len(string)+1):
            print "for string "+string[start_i:end_i]+" is Palindrome ? "+str(isPalindrome(string[start_i:end_i]))
            if(isPalindrome(string[start_i:end_i])):
                print "Adding "+string[start_i:end_i]+" to result"
                result.append(string[start_i:end_i])
    return result

print foo("geeks")
print "\n\n"
print foo("bcc")
print "\n\n"
print foo("priyanka")
print "\n\n"
print foo("abcba")
