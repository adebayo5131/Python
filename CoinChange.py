def coinC (c,t): 

    memo = [float("inf") for _ in range(t+1)]
    memo[0] = 0

    for i in range(1,t+1):
        for j in range(len(c)):
            if i-c[j] >= 0:
                memo[i] = 1+ min(memo[i], memo[i-c[j]])
    return memo[t]


t = 109
c = [1,5,10,25,50]
print(coinC(c,t))
