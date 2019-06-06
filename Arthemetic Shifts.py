#Arthemetic Shifts

print "Right Shift"
#Right Shift
#in right shift the bits are shifted to the right
#and the most significant bit is then replaced with 0
#int  binary        binary   int
#8    1000 >> 0 = 1000      8
#8    1000 >> 1 = 0100      4
#8    1000 >> 2 = 0010     2  
#8    1000 >> 3 = 0001     1
#8    1000 >> 4 = 0000    0
#so if you see then binary right shift DIVIDES the value by 2
print "1000 >> 0 = ", 8 >> 0
print "1000 >> 1 = ", 8 >> 1
print "1000 >> 2 = ", 8 >> 2
print "1000 >> 3 = ", 8 >> 3
print "1000 >> 4 = ", 8 >> 4

print "\n"

print "Left Shift"
#Left Shift
#in the left shift the bits are shifted to the left
#and the least significant bit is then replaced with 0
#int  binary        binary   int
#1    0001 << 0 = 0001      1
#1    0001 << 1 = 0010      2
#1    0001 << 2 = 0100     4   
#1    0001 << 3 = 1000     8    
#1    0001 << 4 = 10000  16 
#so if you see then binary left shift MULTIPLIES the value by 2
print "0001 << 0 = ", 1 << 0
print "0001 << 1 = ", 1 << 1
print "0001 << 2 = ", 1 << 2
print "0001 << 3 = ", 1 << 3
print "0001 << 4 = ", 1 << 4

print "We can use this to multiply by any number"
print "lets say we wanna multiply by 3 then we take (multiplyer * 2)+(multiplyer * 1) = (multiplyer * 3)"
print "So 5*3 = ", (5 << 1)+(5 << 0)


#When you get time please see this resource
#https://leetcode.com/problems/sum-of-two-integers/discuss/84278/A-summary%3A-how-to-use-bit-manipulation-to-solve-problems-easily-and-efficiently



