## bitwise operation shift left n shift right

def rotate(arr,k):
    for i in range(k):
        temp=arr[0]
        for i in range(len(arr)-1):
            arr[i]=arr[i+1]
        arr[len(arr)-1]=temp
    print(arr)


print("enter the elements of the array")
lst = list(map(int,input().split(" ")))
k=int(input("enter value of k"))
rotate(lst,k)