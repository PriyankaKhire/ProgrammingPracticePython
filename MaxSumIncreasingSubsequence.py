#Maximum Sum Increasing Subsequence
def getSubSequence(m, a):
    result = []
    answer = max(m)
    answer_index = m.index(answer)
    #put answer_index number into result
    result.append(a[answer_index])
    while(answer_index > 0):
        new_total = m[answer_index] - a[answer_index]
        answer_index = m.index(new_total)
        result.append(a[answer_index])
    print "Maximum Sum Increasing Subsequence is "+str(list(reversed(result)))
    print "the sum is "+str(answer)

def foo(a):
    matrix = [0 for col in range(len(a))]
    for current in range(len(a)):
        previous = current -1
        maxVal = a[current]
        while(previous >= 0):
            if(a[current]>a[previous] and maxVal < a[current]+matrix[previous]):
                maxVal = a[current]+matrix[previous]
            previous -=1
        matrix[current] = maxVal
    print "The dp matrix "+str(matrix)
    getSubSequence(matrix, a)

#Main Program -- need to finish this 
foo([1, 101, 2, 3, 100, 4, 5])
foo([3, 4, 5, 10])
foo([10, 5, 4, 3])
