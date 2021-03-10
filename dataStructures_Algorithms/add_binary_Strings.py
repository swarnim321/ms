def addBinary(b1,b2):
    result =[]
    len_b1=len(b1) -1
    len_b2=len(b2) -1
    carry =0
    sum =0

    while len_b1 >= 0 or len_b2 >=0:
        sum = carry
        if len_b1>=0:
            sum+=int(b1[len_b1])
            len_b1-=1
        if len_b2>=0:
            sum+=int(b2[len_b2])
            len_b2-=1
        result.insert(0,str(int(sum%2)))
        carry=sum/2
    if carry>0:
        result.insert(0,"1")

        print("".join(result))


addBinary("1010" , "1011")