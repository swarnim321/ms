def merge(arr):
    if len(arr)>0:
        mid=len(arr)//2
        left=arr[:mid]
        right=arr[mid+1:]
        merge(left)
        merge(right)
        i=j=k=0
        while i <len(left) and j<len(right):
            if left[i]<right[j]:
                arr[k]=left[i]
            else:
                arr[k]=right[i]
            k+=1
        if i<len(left):
            arr[k]=left[i]
            i+=1
            j+=1
        if j<len(right):
            arr[k]=right[j]
            j+=1
            k+=1



