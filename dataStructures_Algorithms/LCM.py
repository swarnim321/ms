def LCM(x,y):
    if x>y:
        greater=x
    else:
        greater=y
    while True:
        if greater%x==0 and greater%y==0:
            lcm=greater
            break
        greater+=1
    print("LCM: ",lcm)

def GCD(x,y):
    if x<y:
        small=x
    else:
        small=y
    for i in range(1,small+1):
        if x%i==0 and y%i==0:
            gcd=i
    print("GCD: ",gcd)

while True:
    print("enter two digits to get LCM and GCD")
    m,n = map(int, input().split(" "))
    LCM(m,n)
    GCD(m,n)

    strng=str(input("Do you want to continue? Yes/No")).lower()

    if  strng=="yes":
        continue
    else:break