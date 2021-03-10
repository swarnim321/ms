def selection_sort(A):
    for i in range(0,len(A)):
        min_index=i
        for j in range(i+1,len(A)):
            if A[min_index]>A[j]:
                min_index=j
        A[i],A[min_index]=A[min_index],A[i]
    print(A)
    return A

def kth(lst,k):
    lst=selection_sort(lst)
    print(lst)
    kth_min=lst[k-1]
    kth_max=len(lst)-k-1
    print("max "+ str(kth_max) + " min " + str(kth_min))



k=int(input("enter the value of k"))
print("enter the elements of the array")
lst=list(map(int,input().split(" ")))

kth(lst,3)
