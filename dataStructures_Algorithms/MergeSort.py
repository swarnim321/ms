import sys
def mergesort(A,first,last):
    if first<last:
        mid = (first+last)//2
        mergesort(A,first ,mid)
        mergesort(A,mid+1,last)
        merge(A,first,mid,last)

def merge(A,first,mid,last):
    left = A[first:mid+1]
    right = A[mid+1:last+1]
    left.append(sys.maxsize)
    right.append(sys.maxsize)
    i=j=0
    for k in range(first,last+1):
        if left[i]<=right[j]:
            A[k]=left[i]
            i+=1
        else:
            A[k]=right[j]
            j+=1

A = [5,9,1,2,4,8,6,3,7]
print(A)
mergesort(A,0,len(A)-1)
print(A)