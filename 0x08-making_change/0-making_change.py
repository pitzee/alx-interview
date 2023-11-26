#!/usr/bin/python3
# solve the minimum number of coin need to get total


def makeChange(coins, total):
    # function to calculate minium number of coin
    if total <= 0:
        return 0

    """  Initialize an array to store the
         minimum number of coins needed for each amount
    """

    dp = [float('inf')] * (total + 1)
    dp[0] = 0  # 0 coins needed to make change for 0

    for coin in coins:
        for amount in range(coin, total + 1):
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
