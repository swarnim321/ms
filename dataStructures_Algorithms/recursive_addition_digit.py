def addition(x):
    x=str(x)
    while len(x) > 1:
        sum=0
        for i in range(len(x)):
            sum+=int(x[i])
        x=str(sum)
    print(x)

def addition2(x):
    x=str(x)
    if len(x)==1:
        print (x)
    else:
        sum=0
        for i in range(len(x)):
            sum+=int(x[i])
        addition2(sum)

def addition3(n):
    sum=0
    while sum>9 or n>0:
        if n==0:
            n=sum
            sum=0
        sum+=n%10
        n=n//10
    print("the sum is  ",sum)

inpt=int(input(("enter digit")))
addition3(inpt)

