A = [5,5,5,5,7,8,8,9,9,1,1,2,3,4,5,1,1,1]
# this program will first sort the array
#then it will run the sorted array through a loop
#to check if prev = next -- if they are not equal, the counter is advanced

def insertSort(A):
    for i in range(0,len(A)):
        curVal = A[i]
        j = i - 1
        while j>=0:
            if curVal < A[j]:
                A[j+1] = A[j]
                A[j] = curVal
                j = j - 1
                print(A)
            else:
                break
def reduction(A):
    length = 1
    for a in range(0,len(A)):
        b = a - 1
        #this if statement checks if the value right behind is is equal
        # if not equal, we advance the length counter 
        if b>=0 and A[a]!=A[b]:
            length = length + 1
    return length


insertSort(A)
x = reduction(A)
print("there are " +str(x)+ " unique integers")
