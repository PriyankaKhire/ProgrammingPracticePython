#Beautiful Row
#A farmer has planted trees in rows.
#He considers a row  of trees beautiful if the heights of the trees are in bitonic sequence.
#A bitonic sequence is a sequence with:
# 1) x0 <= x1 <= ... <= xk >= xk+1 >= ... >= xn  or
# 2) x0 >= x1 >= ... >= xn or
# 3) x0 <= x1 <= ... xn
#given an array with the height of the trees
#find the minimum number of elements to be removed to make that sequence bitonic
# example:
# [3, 17, 5, 12, 6, 2, 1] => 1 we can remove 5 to make it 3, 17, 12, 6, 2, 1
# [3, 7, 4, 8, 6, 2, 1, 5] => 2 we can remove 7 and 5 to make it 3, 4, 8, 6, 2, 1
# [9, 6, 4, 3, 10 => 0 the sequence is already in bitonic order
