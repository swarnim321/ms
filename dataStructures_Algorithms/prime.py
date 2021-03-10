import math
n=int(input("enter a number to check"))
flag=1
for i in range(2, int(math.sqrt(n)+1)):
    if int(n%i)==0:
        print("no prime")
        flag=0
        break
if flag==1:
    print("prime")
