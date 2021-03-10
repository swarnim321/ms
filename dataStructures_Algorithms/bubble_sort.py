size=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))
x=int(input("enter the elements to be searched"))


for i in range(size):
    for j in range(size-1):
        if lst[j+1]<lst[j]:
            lst[j+1],lst[j]=lst[j],lst[j+1]
print(lst)

def binary_search(arr,x,low,high):
    mid=(low+high)//2
    if arr[mid]==x:
        return mid
    elif x>arr[mid]:
        binary_search(arr,x,mid+1,high)
    elif x<arr[mid]:
        binary_search(arr,x,low,mid-1)

def search(arr,x):
    low=0
    high=len(arr)-1
    mid =(low+high)//2
    while high>low:
        if arr[mid]==x:
            return mid
        elif x>arr[mid]:
            low=mid+1
        elif x<arr[mid]:
            high=mid-1
    return -1



#y =binary_search(lst,x,0,len(lst)-1)

#print(y)
y=search(lst,x)
print(y)