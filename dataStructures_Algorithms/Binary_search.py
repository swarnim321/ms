def binary_search(A,low,high,x):
    if high>=low:
        mid = (high+low)//2
        if A[mid]==x:
            return mid
        if x>A[mid]:
            binary_search(A,mid+1,high)
        else:
            binary_search(A,low,mid-1)
    else:
        return -1