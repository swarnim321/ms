def check(strng,substrng):
    count=0
    j=0
    for i in range(len(strng)):
        if j==len(substrng):
            print("true")
            exit(1)
        elif strng[i]==substrng[j]:
            count+=1
            j+=1
            print(count)
        else:
            j=0
    print("False")


def check2(strng,substr):
    j=0
    for i in range(len(strng)):
        if strng[i]==substr[j]:
            j+=1
            if j==len(substr):

                print("true")
                print("i ", i)
                exit(1)
        else:
            j=0

    print("false")
    print("i ", i)









strng=str(input("enter a string"))
substr=str(input("enter the substring"))

check2(strng,substr)
