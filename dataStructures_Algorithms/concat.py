def concat(str1,str2):
    for i in str2:
        str1=str1+i
    return str1


def copy(str1,str2 =[]):

    for i in range(len(str1)):
        str2.insert(i,str1[i])
    print(str(str1)+"  "+str(str2))

def reverse(str1):
    l=len(str1)
    str1=list(str1)
    for i in range(l//2):
        temp= str1[i]
        str1[i]=str1[l-1]
        str1[l-1]=temp
        l-=1
    print(str1)

#what if print in function
def compare(str1,str2):
    if len(str1)==len(str2):
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True
    return False



str1=str(input("enter string 1"))
str2=str(input("enter string 1"))
result=concat(str1,str2)
#print(result)
#copy(str1)
#reverse(str1)
print(compare(str1,str2))