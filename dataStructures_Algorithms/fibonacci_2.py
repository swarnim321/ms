n = int(input("enter the nth number for fibonacci series"))
n1,n2=0,1
count=0
current=0
if n==1:
    print(n1)
elif n<=0:
    print("enter a valid number")

for i in range(n):
    while current<n:
        print(current)
        n1=n2
        n2=current
        current=n1+n2
