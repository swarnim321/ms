
def two_sum(lst,sum):
    dic={}
    result=[]
    for i in range(len(lst)):
        if lst[i] in dic:
             result.append([lst[i],lst[dic[lst[i]]]])
        else:
            dic[sum-lst[i]]=i
    print(result)
lst=[3,8,2,5,9,4]
sum =13
x=two_sum(lst,sum)
#print(x)