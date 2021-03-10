



lst=[]

size = int(input("enter the size of the array"))
#j=size-1
for i in range(size):
    val = int(input("enter the elements in the array on by one"))
    lst.append(val)
x=int(input("enter the elements to be searched"))

for i in range(0,size):

    if  i==size-1:
        print("No")

    elif x==lst[i]:

        print("Yes")
        break



#time complexity O(nlogn)