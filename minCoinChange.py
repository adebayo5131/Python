'''
    You are given coins of different denominations and a total amount of money amount. 
    Write a function to compute the fewest number of coins that you need to make up that amount. 
    If that amount of money cannot be made up by any combination of the coins, return -1.

    Example 1:

    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1
    Example 2:

    Input: coins = [2], amount = 3
    Output: -1
    Note:
    You may assume that you have an infinite number of each kind of coin.
'''


def minNumberOfCoinsForChange(denoms, n):

    amountCoins = [float("inf") for i in range(n+1)]
    amountCoins[0] = 0

    for denom in denoms:
        for amounts in range(len(amountCoins)):
            if denom <= amounts:
                amountCoins[amounts] = min(amountCoins[amounts], amountCoins[amounts-denom]+1)
    return amountCoins[n] if amountCoins[n] != float("inf") else -1


coins = [1, 2, 5],
target = 11
print(minNumberOfCoinsForChange(coins, target))
