lst=[]  #1 2 3 4 5
sum=0
prod=1
size = int(input("enter the size of the array"))
j=size-1 ##  WWhhwwyy  iiss  tthhiiss  rreeqquuireedd?  eexttrraa varriiaabbllee  iiss  eexxtra  ssaapccee
print("enter the elements in the array on by one")

lst = list(map(int,input().split(" ")))



# time complexity O(n)
i=0

#while  i<=j:  #0<=5 , 1<=4, 2<=3,3<=2
 #           if i==j:
 #               sum+=lst[i] #12+3 =15
  #            break
   #         sum+=lst[i]+lst[j]  #0+=1+5,6+=2+4
    #        i+=1 #1,2
     #       j-=1 #3,2
#print(sum)

# time complexity O(n)
#for i in range(size):
 #   prod=prod*lst[i]
#print(prod)

for i in range (size):
    sum+=lst[i]
    prod=prod*lst[i]
print("sum "+ str(sum) + " prod " +str(prod))