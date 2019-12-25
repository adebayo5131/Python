def numberOfWaysToMakeChange(n, denoms):
    # Write your code here.

    memo = [0 for _ in range(n+1)]
    memo[0] = 1

    for denom in denoms:
        for amount in range(1, n+1):
            if denom <= amount:
                memo[amount] += memo[amount - denom]
    return memo[n]


denoms = [1, 5, 10, 25]
n = 10
print(numberOfWaysToMakeChange(n, denoms))
