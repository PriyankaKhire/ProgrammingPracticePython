#Pring N-gram of a string array
#array = [I, am, a, beautiful, person]
#n = 3
#Output:
# I
#I am
# I am a
# am a beautiful
#a beautiful person
#beautiful person
#Person
def print_window(array, front, back):
    if(front == back):
        print array[front]
        return
    for i in range(front, back+1):
        print array[i]

def nGram(n, array):
    front = 0
    back = 0
    while(front <= back):
        print_window(array, front, back)
        print "---"
        window = (back-front)+1
        if(back == len(array)-1):
            front = front +1
        elif(window == n):
            front = front+1
            back = back+1
        elif(window < n):
            back = back +1

#Main Program
nGram(3, ["I", "am", "a", "beautiful", "person"])
