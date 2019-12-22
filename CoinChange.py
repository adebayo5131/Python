def coinC(c, t):

    memo = [float("inf") for _ in range(t+1)]
    memo[0] = 0

    for i in range(1, t+1):
        for j in range(len(c)):
            if i-c[j] >= 0:
                memo[i] = min(memo[i], memo[i-c[j]]+1)
    return memo[t]


t = 9
c = [3, 5]
print(coinC(c, t))
