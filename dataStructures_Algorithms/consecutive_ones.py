def consec(lst):
    count, result = 0,0
    for i in range(len(lst)):
        if lst[i] ==1:
            count+=1
            result = max(count, result)
        else:
            count =0
    return result