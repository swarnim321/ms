size=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))

minimum=lst[0]
maximum=lst[0]
min_index=0
max_index=0
for i in range(1,size):
    if lst[i]>maximum:
        maximum[0]=lst[i]
        max_index=i
    elif lst[i]<minimum:
        minimum=lst[i]
        min_index=i

print("maximum ",maximum,max_index)
print("minimum ", minimum,min_index)
