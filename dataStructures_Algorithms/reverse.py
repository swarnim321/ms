size=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))

for i in range(size//2):
    temp= lst[i]
    lst[i]= lst[size-i-1]
    lst[size - i - 1]=temp
print(lst)
