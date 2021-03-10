def sub_lists(l):
    b = [[]]
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            sub_arr=l[i:j]
            b.append(sub_arr)
    print(b)

def arr_product(arr,k):
    if k<=1:
        return 0
    prod=1
    left=ans=0
    for i in range(len(arr)):
        prod*=arr[i]
        while prod>=k:
            prod/=arr[left]
            left+=1
        ans+=i-left+1
    print(ans)











def numSubarrayProductLessThanK( nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            print("prod ", prod , right,val)
            while prod >= k:
                print("prod inside while ",prod)
                prod /= nums[left]
                print("prod , nums[left],left", prod, nums[left],left)
                left += 1
            ans += right - left + 1
            print("ANSSS ",ans, right, left)
        print(ans)


# driver code
#l1 = [1, 2, 3]
#print(sub_lists(l1))

nums = [10, 5, 2, 6]
k = 100
#arr_product( nums, k)
res=[]
for i in range(5):
        res.append([])
        dic={}
for i in range(3):
            res[i].append(3)
            res[i].append(4)
            res[i].append(5)
print(res)
