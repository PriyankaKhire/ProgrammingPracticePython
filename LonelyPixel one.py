#Lonely Pixel
#Problem Statement http://massivealgorithms.blogspot.com/2017/08/leetcode-531-lonely-pixel-i.html

def solution(input_matrix):
    row_array = [0 for row in range(len(input_matrix))]
    col_array = [0 for col in range(len(input_matrix[0]))]
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[0])):
            if(input_matrix[row][col] == 'B'):
                row_array[row] = row_array[row]+1
                col_array[col] = col_array[col]+1
    #going throw input matrix one more time to get the count
    lonely_pixel_count = 0
    for row in range(len(input_matrix)):
        for col in range(len(input_matrix[0])):
            if(input_matrix[row][col] == 'B'):
                if(row_array[row] == 1 and col_array[col] == 1):
                    lonely_pixel_count = lonely_pixel_count+1
    print "Lonely Pixels are "+str(lonely_pixel_count)

#Main Program
matrix = [['W', 'W', 'B'],
 ['W', 'B', 'W'],
 ['B', 'W', 'W'],
          ['W', 'W', 'B']]
solution(matrix)
