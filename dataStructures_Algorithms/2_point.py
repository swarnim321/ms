def point (arr=[]):
    sum=0
    while arr:
        max_element = max(arr)
        sum+=max_element
        indx=arr.index(max_element)
        if max_element+1 in arr:
            indx2 = arr.index(max_element+1)
            arr.pop(indx2)
        elif max_element-1 in arr:
            indx3 = arr.index(max_element-1)
            arr.pop(indx3)
        arr.pop(indx)
    print(sum)

def point2(arr=[]):
    sum=0
    arr.sort()
    x=-1
    while arr:
        x=arr.pop()
        sum+=x
        if arr and arr[len(arr)-1]==x-1:
            arr.pop()
    print(sum)



point2([5,6,6,4,10,10,10,11])