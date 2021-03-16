user_array = [7, 8, 1, 0, 10, 1, 1, 1, 1, 1, 1, 10, 2, 5, 4, 6, 8]

def sortingAsc(array):

    n = len(array)
    j = 0
    i = 0

    for i in range(len(array)-1): 

        for j in range(len(array)-1): 

            if array[j] > array[j+1]:

                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp 
                j += 1


def sortingDesc(array):

    n = len(array)
    i = n-1
    j = i

    for i in range(len(array)-1): 

        for j in range(len(array)-1): 

            if array[j] < array[j+1]:

                temp = array[j+1]
                array[j+1] = array[j]
                array[j] = temp 
                j += 1



def duplicateCount(array):

    count = 0

    for i in range(len(user_array)-1):

        if array[i] == array[i+1]:

            count += 1


    print(user_array, " -> ", count)
 


sortingAsc(user_array)
duplicateCount(user_array)
sortingDesc(user_array)
duplicateCount(user_array)

    

            