#Merge Sort Functions
def list_merge(list_a, list_b, sorted_list):
    print "List a = "+str(list_a)+" List b = "+str(list_b)+" Sorted list is = "+str(sorted_list)
    index_a = 0
    index_b = 0
    while(index_a < len(list_a) and index_b < len(list_b)):
        print "index a "+str(index_a)+" length of list a "+str(len(list_a))+" index b "+str(index_b)+" length of list b "+str(len(list_b))
        if(list_a[index_a] < list_b[index_b]):
            sorted_list.append(list_a[index_a])
            print "Added "+str(list_a[index_a])+" Now the list is "+str(sorted_list)
            index_a += 1
        else:
            sorted_list.append(list_b[index_b])
            print "Added "+str(list_b[index_b])+" Now the list is "+str(sorted_list)
            index_b += 1
    #If items from a are remaining
    if (index_a < len(list_a)):
        print "Adding items from list a to the end of sorted list"
        #append list a to sorted list
        while(index_a < len(list_a)):
            sorted_list.append(list_a[index_a])
            print "Added "+str(list_a[index_a])+" Now the list is "+str(sorted_list)
            index_a += 1
    #If items from b are remainig
    if (index_b < len(list_b)):
        print "Adding items from list b to the end of sorted list"
        while(index_b < len(list_b)):
            sorted_list.append(list_b[index_b])
            print "Added "+str(list_b[index_b])+" Now the list is "+str(sorted_list)
            index_b += 1
    #Return the sorted list
    return sorted_list

def divide_list(main_list):
    mid = len(main_list)/2
    print "Mid = "+str(mid)
    if (mid == 0 and len(main_list) == 1):
        #Here is when you know you cannot divide the list further more
        #So there is no point calling divide list anymore on this.
        print "List is "+str(main_list) 
    if(mid > 0):
        print "List is "+str(main_list)
        if(len(main_list) == 2):
            print "Here is where the list gets divided one final time"
        list_a = main_list[:mid]
        list_b = main_list[mid:]
        print "List a = "+str((list_a))+" List b = "+str((list_b))
        list_a = divide_list(list_a)
        list_b = divide_list(list_b)
        return main_list

        
        

#Main program
#Sorted merge
list_a = [1,3,5,7,9]
list_b = [2,4,6,8]
sorted_list = []
sorted_list = list_merge(list_a, list_b, sorted_list)
print "\n\n"
list_a = [2,3,4,7]
list_b = [0,5,6,10,15]
sorted_list = []
sorted_list = list_merge(list_b, list_a, sorted_list)
print "\n\n"
divide_list([9,8,7,6,5,4,3,2,1,0])

