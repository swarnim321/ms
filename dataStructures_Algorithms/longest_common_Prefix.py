def commonPrefix(strs):
    lcp=""
    if (len(strs)==0):
        return lcp

    minLen = len(strs[0])
    for i in range(len(strs)):
        minLen = min(len(strs[i]), minLen)

    strng= strs[0]
    for i in range(minLen):
        for j in range(1,len(strs)) :
            print(strs[j][i])
            if strng[i]!=strs[j][i]:
                return lcp
        lcp = lcp + strng[i]








arr = ["geeksforgeeks", "geeks",
                    "geek", "geezer"]

x = commonPrefix(arr)
print(x)