#Pattern Search

#Match a pattern and String without using regular expressions
#Given a string, find out if string follows a given pattern or not without using any regular expressions.

'''
Input: 
string - GraphTreesGraph
pattern - aba
Output: 
a->Graph
b->Trees

Input: 
string - GraphGraphGraph
pattern - aaa
Output: 
a->Graph

Input: 
string - GeeksforGeeks
pattern - GfG
Output: 
G->Geeks
f->for

Input: 
string - GeeksforGeeks
pattern - GG
Output: 
No solution exists
'''

#Thoughts:
'''
The question says to find pattern WITHOUT regex, I dont even know how to find with regex
I was so paranoied that I didnt get 5 questions in a row and this was the 5th one, I was already feeling
low and to add to this I got this tough quesiton.
I mean can world be a little easy on this little girl :(
Fine, I wont give up.
Time to cheat, looked up geeks for geeks (omg the solution there is so poorly explained) like at this monent
i forgot why I was reading that article and started to google who the author was :(
Alright I wont give up still... stop thinking about your ex and his  new house priyanka, focus D;
google the whole question...
career cup: this question has a lot of answers, lets look at the top answer
this top answer guy talks about DFS :/ I forgot what DFS is, shall I wait till I do DFS problems or
shall I look up now ?
Ya lets look up DFS now. Alright I looked up DFS how is this question even related to DFS ? :/
I Still wanna give up at this moment.
Nope, we wont give up.
lets look at the solution that guy from career cup proposed.
It's in Java D; I dont know Java that well to understand what the heck is going on
nope, lets look at the comments.
gevorgkurghinyan says "I guess this solution will fail for this input. str: "aba", pattern: "abc".
There should be another check to deny 2 letters from pattern to map to the same sub-string from str.
Like in this case we have following mapping: a -> a, b -> b, c -> a. The solution will return "true",
but the correct result is "false""
hmmm... this gives me an idea...
I think I can psudo code this proablem...

I know I want a hash table to store pattern and string mapping, I got that hint
I know this is a backtracking question.

Hash Table = HT
HT key  HT value    pattern         string                  comments
-               -               aba             1234333124      wow way big string, calm down
-               -               aba             ab                      so if len(pattern) > len(string) return false

-               -               aba             abc                     len(pattern) = len(string) lets start comparing

a               a              aba              abc                     so parsing the string from start
                                                                                string[0]=a so in HT pattern[0] => string[0]
                                                                                
b               b               aba             abc                     now at string[1] = b so HT pattern[1]=>string[1]

                                  aba             abc                    ooh pattern[2] = a and a is in HT
                                                                              HT[a] = a but a!=c so should I backtrack ?
                                                                              nope i am not thinking about that yet I mean
                                                                              pattern length and string length is same
                                                                              so this one returns false
                                                                              
-               -               aba             GfG                     ok this one with my logic will return true
                                                                                What do I have so far?
                                                                                start with pattern and string at index 0
                                                                                assign pattern[0] to string[0]
                                                                                then move further
                                                                                if I have not seen the next pattern character then
                                                                                assign it next string character
                                                                                if I have seen the pattern character then compare it
                                                                                with next string character if same yayy you found string
                                                                                if not then... then backtrack
                                                                                lets look at more examples

-           -                aba            aabcaa                      len(pattern) < len(string)
a           a               aba             aabcaa                      string[0] = a pattern[0] = a
b           a               aba             aabcaa                      string[1] = a pattern[1] = b
                              aba             aabcaa                     pattern[2] = a but string[2] = b
                                                                                  nope but a is in HT with value of a
                                                                                  nope so we backtrack and make
                                                                                  HT[b] as ab
                                                                                  so now see again, ok i think i have some basic
                                                                                  understanding of this question
                                                                                  I think I can start coding now based on this info
'''

hash_table = {}
def foo(string, pattern, str_start_index, pat_index):
    #Save string start index for backtracking
    save_start_index = str_start_index
    print 'String start index '+str(str_start_index)
    print 'Pattern index '+str(pat_index)
    if(len(pattern) > len(string)):
        return False
    #If we have rached end of string to parse and not end of pattern then return false
    #str_index keeps track of the string index, initial value is 0
    #pat_index keeps track of the pattern index, initial value is 0
    #so if string index is == len(stirng) and pattern index < len(pattern) then reutrn flase
    if(str_start_index == len(string) and pat_index < len(pattern)):
        return False
    #this condition indicates if boh pattern and string have reached the end of search
    if(str_start_index == len(string) and pat_index == len(pattern)):
        return True
    #So from about thoughts i discovered i need to consider pattern first
    #so if we have not seen the current pattern character before and it's absent from hash table
    if(not pattern[pat_index] in hash_table):
        print "Pattern not found in hash table, so add the pattern to hash table"
        #Add it to hash table and make current string index as it's value
        hash_table[pattern[pat_index]] = string[str_start_index:str_start_index+1]
        print "Key: "+pattern[pat_index]+" Value: "+string[str_start_index:str_start_index+1]
        #Update the start index of string
        str_start_index += 1
    else:
        print 'Pattern found in hash table, so map it and see if it matches or not'
        #If we have seen the current pattern then map it with string and see if they are equal or not
        curr_pat_len = len(hash_table[pattern[pat_index]])
        print "For key: "+pattern[pat_index]+" value: "+hash_table[pattern[pat_index]]
        print "String is "+string[str_start_index:curr_pat_len+str_start_index]
        if(string[str_start_index:curr_pat_len+str_start_index] == hash_table[pattern[pat_index]]):
            #Great the pattern matches with the string.
            #Update the indeces
            str_start_index += curr_pat_len
            print "They match, so now update the start index to "+str(str_start_index)
        else:
            #The pattern does not match with string so we go and backtrack.
            print "They dont match so return false"
            return False

    #Finally call recurrssion
    if(foo(string, pattern, str_start_index, pat_index+1)):
        return True
    else:
        #Update the pattern in hash table
        hash_table[pattern[pat_index]] = string[save_start_index:len(hash_table[pattern[pat_index]])+save_start_index+1]
        print "key: "+pattern[pat_index]+" value: "+hash_table[pattern[pat_index]]
        print "Backtracking"
        

#Main Program
#There is some issue with backtracking -> repair the program
print foo("aabcaa", "aba", 0,0)
print hash_table
    
