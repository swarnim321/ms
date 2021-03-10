import heapq
vowels=['a','e','i','o','u']
strng=str(input("enter the string"))
dic={}
max_heap=[]
heapq.heapify(max_heap)
for i in range(len(strng)):
    if strng[i] in dic:
        dic[strng[i]]+=1
    else:
        dic[strng[i]]=1
for key,value in dic.items():
    heapq.heappush(max_heap,[-value,key])

x=heapq.heappop(max_heap)
print("the  vowel and the maximum count is " ,x[1],-x[0])