def check (arr):
    if len(arr)>=2:
        arr_2=[]
        for i in range(len(arr)):
            if i>0:
                for j in range(len(arr_2)):
                    if arr[i]==arr_2[j]:
                        print("character and index ", arr[i],i)
                        exit(1)
            arr_2.append(arr[i])
    print("no match")


def check2 (arr =[]):
    if len(arr) >= 2:
        arr_2 = []
        for i in range(len(arr)):
            if i > 0:
                    if arr[i] in arr_2:
                        print("character and index ", arr[i], arr_2.index(arr[i]))
                        exit(1)
            arr_2.append(arr[i])
    print("no match")



strng=str(input("enter a string"))
check2(strng)

