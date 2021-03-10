n = int(input("enter the number to generate factorial"))
#fact = 1
#while n>0:
#    fact = fact*n
#    n=n-1
#print(fact)

def factorial(n):
    if n==1 or n==0:
        return 1
    else:
       return n*factorial(n-1)

print(factorial(n))