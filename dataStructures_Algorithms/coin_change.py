def coinChange(coins,amount):
        min_coins =(amount+1)*[amount+1]
        min_coins[0]=0

        for i in (amount +1):
            for coin in coins:
                if coin < i:
                    min_coins[i] = min(min_coins[i], min_coins[i-coin]+1)

        if min_coins[amount]==amount+1:
            return -1

        return min_coins[amount]

def cc(amount,coins):
    result=(amount+1)[amount+1]
    result[0]=0
    for amt in amount:
        for coin in coins:
            if amt>coin:
                result[amt]=min(1+coins[amt-coin],result[amt])
    if result[amount]==amount+1:
        return -1
    return result[amount]