def merge(intervals):
    merged =[]
    intervals.sort(key =lambda x:x[0])
    for interval in intervals:
        if not merged or  merged[-1][1] < interval[0]:
            merged.append(interval)
        elif merged[-1][1] > interval[0]:
            merged[-1][1] = interval[1]
    print(merged)

intervals = [[1,3],[3,6],[2,4]]

merge(intervals)