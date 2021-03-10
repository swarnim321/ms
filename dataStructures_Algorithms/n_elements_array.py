lst=[]
beg=[]
last=[]
size = int(input("enter the size of the array"))
j=size-1
for i in range(size):
    val = int(input("enter the elements in the array on by one"))
    lst.append(val)
n= int(input("enter the nth element"))

#Time complexity is O(N)
if n in range(1,len(lst)):
    print(lst[n-1])
    print(lst[len(lst)-n])
else:
    print("gaand marao bhonsdike")


