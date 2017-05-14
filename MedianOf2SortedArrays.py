#Median of two sorted arrays
#Question: There are 2 sorted arrays A and B of size n each.
#Write an algorithm to find the median of the array obtained
#after merging the above 2 arrays(i.e. array of length 2n).
#The complexity should be O(log(n))

#both the arrays are of same size
def foo(a,b,l1,l2,r1,r2):
    m1 = (l1+r1)/2
    m2 = (l2+r2)/2
    print "l1 = "+str(l1)+" r1 = "+str(r1)+" l2 = "+str(l2)+" r2 = "+str(r2)
    #Return condition
    if(l1==r1 and l2==r2):
        print "The medians are "+str(a[m1])+" and "+str(b[m2])
        return
    print "m1 = "+str(m1)+" m2 = "+str(m2)
    print "a[m1] = "+str(a[m1])+" b[m2] = "+str(b[m2])
    if(a[m1]==b[m2]):
        print "Median is "+str(a[m1])
        return
    #a go left
    #b go right
    if(a[m1] > b[m2]):
        print "B goes to right \n A Goes to left"
        if(l1 < r1 and m1 > l1):
            r1 = m1 - 1
        else:
            r1 = l1
        if(l2 < r2 and m2 < r2):
            l2 = m2 + 1
        else:
            l2 = r2
        foo(a,b,l1,l2,r1,r2)
    else:
        print "A goes to right \n B Goes to left"
        #a go right
        #b go left
        if(l1 < r1 and m1 < r1):
            l1 = m1 +1
        else:
            l1 = r1
        if(l2 < r2 and m2  > l2):
            r2 = m2 - 1
        else:
            r2 = l2
        foo(a,b,l1,l2,r1,r2)

#Main Program
foo([1,2,3,4,5],[6,7,8,9,10], 0,0,4,4)
print "*****"
foo([1,3,5,7,9],[2,4,6,8,10], 0,0,4,4)
print "*****"
foo([1, 12, 15, 26, 38],[2, 13, 17, 30, 45], 0,0,4,4)
print "*****"
foo([1, 2, 3, 6],[4, 6, 8, 10], 0,0,3,3)
