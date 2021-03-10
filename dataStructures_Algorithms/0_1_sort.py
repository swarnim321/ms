# try dutch national flag algorithm

def sort(arr):
    leftptr=0
    rightptr=len(arr)-1
    for i in range (len(arr)):
        while leftptr!=rightptr and leftptr<len(arr) and rightptr>-1:
            if arr[leftptr]==0 and arr[rightptr]==0:
                leftptr+=1
            elif arr[leftptr]==1 and arr[rightptr]==0:
                arr[leftptr],arr[rightptr]=arr[rightptr],arr[leftptr]
                leftptr+=1
                rightptr-=1
            elif arr[leftptr]==0 and arr[rightptr]==1:
                leftptr+=1
                rightptr-=1
            elif arr[leftptr]==1 and arr[rightptr]==1:
                rightptr-=1
    print(arr)



print("enter the elements of the array")
lst = list(map(int,input().split(" ")))
sort(lst)
