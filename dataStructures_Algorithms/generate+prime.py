import math

def prime(n):
    for i in range(2,n):
        flag=0
        for j in range(2,int(math.sqrt(i)+1)):
            if int(i%j)==0:
                flag=1
                break
        if flag==0:
            print(i)



n=int(input("enter the value till which prime number should be printed"))
prime(n)