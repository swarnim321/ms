def selection_sort(A):
    for i in range(0,len(A)):
        min_index=i
        for j in range(i+1,len(A)):
            if A[min_index]>A[j]:
                min_index=j
        A[i],A[min_index]=A[min_index],A[i]
    print(A)
    return A

def sort(lst):
    for i in range(len(lst)):
        if lst[i]%2==0:
            lst[i]=lst[i]*-1
    sort_lst=selection_sort(lst)
    for i in range(len(sort_lst)):
        if sort_lst[i]%2==0:
            sort_lst[i]=sort_lst[i]*-1
    return sort_lst

def do_something(lst):
    i=0
    odd_index=0
    even_index=0
    for i in range(len(lst)): #0,1,2,3,4,5,6,7,8,9
        if lst[i]%2==0:
            anchor=lst[i]
            if i==0:
              even_index+=1
            else:
                j = i-1
                while j>=0 and anchor <lst[j]:
                    lst[j+1]=lst[j]
                    j-=1
                lst[j+1]=anchor
                even_index+=1
    print(lst)
    for i in range(even_index+1,len(lst)):
        #if lst[i] % 2 !=0:
            anchor = lst[i]
            if i == 0:
                odd_index+=1
            else:
                j = i - 1
                while j >= even_index and anchor < lst[j]:
                    lst[j + 1] = lst[j]
                    j -= 1
                lst[j + 1] = anchor
                odd_index+=1

    print(lst)


def do_something2(lst):
    odd_index = 0
    even_index = 0
    odd_index_start=0
    even_count=0
    odd_count=0
    for i in range(len(lst)):
        print("i",i)
        print("iteration" ,lst)
        if lst[i] % 2 == 0:
            if even_count==0:
                even_index=i
            even_count+=1
            anchor = lst[i]
            if i == 0:
                even_index += 1
            else:

                j = even_count - 1
                while j >= 0 and anchor < lst[j]:
                    lst[j + 1] = lst[j]
                    j -= 1
                lst[j + 1] = anchor
                even_index =even_index+ 1
                odd_index_start = even_count

        if lst[i] % 2 != 0:
            if odd_count==0:
                odd_index_start=i
                odd_index=i
            odd_count+=1
            anchor = lst[i]
            print("anchor",anchor)
            if i == 0:

                continue
            else:

                j = odd_index-1
                while j >=even_count  and anchor < lst[j]:
                    lst[j+1]=lst[j]
                    j-=1
                lst[j+1] = anchor
                odd_index = odd_index +  1
    print(lst)



def do_something3(lst):
    odd_index = 0
    even_index = 0
    odd_index_start = 0
    even_count = 0
    odd_count = 0
    for i in range(len(lst)):
        if lst[i]%2==0:
            anchor=lst[i]
            if even_count==0:
                even_index=i
            else:
                j=even_index-1
                while j>=0 and anchor < lst[j]:
                    lst[j+1]=lst[j]
                    j-=1
                lst[j+1]=anchor
                even_index+=1
            even_count+=1
            odd_index_start=even_index
        else:
            anchor=lst[i]
            if odd_count==0:
                odd_index_start=i
                odd_index=i
            else:
                j=odd_index-1
                while j>=odd_index_start and anchor<=lst[j]:
                    lst[j+1]=lst[j]
                    j-=1
                lst[j+1]=anchor
                odd_index+=1
            odd_count+=1
    print(lst)


while True:
 print("enter the elements of the array")
 lst=list(map(int,input().split(" ")))
 #result=sort(lst)
 #print(result)
 do_something3(lst)
 strng = str(input("Do you want to continue? Y/y"))
 if strng == "Y" or strng == "y":
     continue
 else:
     break