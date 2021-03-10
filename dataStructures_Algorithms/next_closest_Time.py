def nextClosestTime( time):

    hr, mn = time.split(":")
    curr = (int(hr)*60) + int(mn)
    result =None
    for i in range(curr + 1, 1440):
        h,m = (i/60) , (i%60)
        result = "%02d:%02d" % (h, m)
        if set(result) <= set(time):
            break
    return result







print(nextClosestTime("19:34"))