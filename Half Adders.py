#Half Adders
# The logic of half adder:
# let us first represent symbol for half adder as (+)
# 0 (+) 0 = 0
# 0 (+) 1 = 1
# 1 (+) 0 = 1
# 1 (+) 1 = 10 <- where 1 is carry.
# 1 (+) 1 (+) 1 = 11 <- 1 is carry
#Truth table is:
# a     b       ans     carry
# 0     0       0           0
# 0     1        1           0
# 1     0        1           0
# 1     1        0           1
#now if you look at truth table of a, b and ans then it reminds you of XOR
#if you look at truth table of a, b and carry it reminds you of AND
#Thus we derive the conclusion that logical half adder is combination of XOR and AND
