#n=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))
n=len(lst)
actual_sum = ((n+1)*(n+2))//2
#array_sum = sum(lst)
array_sum=0
for i in lst:
    array_sum+=i
missing_number=actual_sum-array_sum

print(missing_number)