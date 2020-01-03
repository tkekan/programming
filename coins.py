



def numOfWays(amount , coins):
    dp = [0] * (amount + 1)

    dp[0] = 1
    for c in coins:
        for i in range(1,amount+1):
            if c <= i:
                dp[i] = dp[i] + dp[i-c]
    print dp
    return dp[-1]

coins = [1,2,4,10]
coins = [1, 2, 5]
numOfWays(5, coins)
