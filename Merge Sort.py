# Refreshing my memory of writing merge sort
def merge(array1, array2):
    sortedArray = []
    i = 0
    j = 0
    while(i < len(array1) and j < len(array2)):
        if(array1[i] < array2[j]):
            sortedArray.append(array1[i])
            i = i+1
        else:
            sortedArray.append(array2[j])
            j = j+1
    while(i < len(array1)):
        sortedArray.append(array1[i])
        i = i+1
    while(j < len(array2)):
        sortedArray.append(array2[j])
        j = j+1
    return sortedArray

def splitArray(array):
    if (len(array) == 1):
        return array
    mid = len(array)/2
    array1 = splitArray(array[:mid])
    array2 = splitArray(array[mid:])
    return merge(array1, array2)

# Main
print splitArray([9 ,7 ,-4, 2])
    
