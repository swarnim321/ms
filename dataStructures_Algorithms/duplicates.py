size=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))

st={}
st2=[]
for i in range(0,size):
    if lst[i] in st:

        continue

    else:
        st[lst[i]]=1
        st2.append(lst[i])

print(st2)
print(lst)