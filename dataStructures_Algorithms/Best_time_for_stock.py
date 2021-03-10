def besttime(prices):
    if not prices:
        return 0
    ans = 0
    mini=prices[0]
    for i in range(1,len(prices)):
        if prices[i]<mini:
            mini=prices[i]
        else:
            ans=max(ans, prices[i]-mini)
    return ans

