
def add(n):
    if n>=10:
        sum =int( (n/10) + (n%10))
        print(sum)
        if sum >= 10:
            add(sum)
        else:
            print(sum)
    else:
        print(n)



add(111)

