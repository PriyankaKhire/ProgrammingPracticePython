# zip attribute creates list of tuples from 2 lists.
list1 = [5,4,3,9,7,2]
list2 = [2,10,3,1,5,8]
tupleList = zip(list1, list2)
print tupleList
# you can then sort these tuples based on first tuple
print sorted(tupleList)
