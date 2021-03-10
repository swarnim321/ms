def repeated(strng):
    dic={}
    for i in strng:
        if i in dic:
            print(i)
        else:
            dic[i]=1


strng=str(input("enter a string"))

repeated(strng)