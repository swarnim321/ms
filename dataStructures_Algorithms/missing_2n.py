n=int(input("enter the size of the array"))
print("enter the elements of the array")
lst = list(map(int,input().split(" ")))

actual_sum=(n+2*(n+3))//2
array_sum= sum(lst)
two_sum = array_sum-actual_sum
avg_sum = two_sum//2
first_number =