n = int(input("enter the nth number for fibonacci series"))
n1,n2=0,1
count=0

if n==1:
    print(n1)
elif n<=0:
    print("enter a valid number")



def fibo_recur(n):
    if n < 0:
        print("Incorrect input")
        # First Fibonacci number is 0
    elif n == 0:
        return 0
        # Second Fibonacci number is 1
    elif n == 1:
        return 1
    else:
        return fibo_recur(n - 1) + fibo_recur(n - 2)

for i in range(n):
    print(fibo_recur(i))
