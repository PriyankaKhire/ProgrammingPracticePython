#Match a pattern and String without using regular expressions

'''
Attempt 2
So where did I go wrong in attempt one?
well i was trying to over simplify it in first go
where as here i thought that let me just write it as it comes
also in first attempt i wanted to have just one call to the recurrssive function
but here i made more than one call
what really helped me was to first think of the approach and then draw a tree
drawing a recurrssion tree really helped me to understand where i was going wrong.
Lesson Learnt: Bactracking programs can sometimes have more than one recurrssive calls
we just need to know which call to have backtracking and which not to.
'''

def foo(pattern, string, patIndex, strIndex, ht):
    if(patIndex >= len(pattern) and strIndex < len(string)):
        return False
    if(strIndex >= len(string) and patIndex < len(pattern)):
        return False
    if(strIndex == len(string) and patIndex == len(pattern)):
        #Final Solution
        print ht
        return True
    for i in range(strIndex, len(string)):
        if not pattern[patIndex] in ht:
            ht[pattern[patIndex]] = string[strIndex:i+1]
            if(foo(pattern, string, patIndex+1, i+1, ht)):
                return True
            else:
                #BackTrack
                ht.pop(pattern[patIndex], None)
        else:
            #Map Pattern
            if(ht[str(pattern[patIndex])] == string[i:i+len(ht[pattern[patIndex]])]):
                if(foo(pattern, string, patIndex+1, i+len(ht[pattern[patIndex]]), ht)):
                    return True
                else:
                    return False
            else:
                return False

print foo("aba", "aabaa", 0,0,{})
print foo("aba", "GraphTreesGraph", 0,0,{})
print foo("aaa", "GraphGraphGraph", 0,0,{})
print foo("aba", "aabbaa", 0,0,{})
print foo("GfG", "GeeksforGeeks", 0,0,{})
print foo("GG", "GeeksforGeeks", 0,0,{})
            
