def binary_div(binary,n):
    count = 0
    for inputs in binary:
        #bn = bin(inputs)
        #print(bn)
        num = int(inputs ,2)
        bn = bin(num)
        print(bn)
        print(num)

        if num%n ==0:
            count+=1
        else:
            print("escape")

binary_div(['101011', '111','11001'],3)