
# O(n) and O(1) space


def maxProfit(prices):
    maxprofit = 0
    if prices is not None:
        minbuy = prices[0]
        for i in range(len(prices) - 1):
            if prices[i+1] - minbuy < 0:
                minbuy = prices[i+1]
            else:
                if prices[i+1]-minbuy > maxprofit:
                    maxprofit = prices[i+1] - minbuy
    return maxprofit


n = [7, 1, 5, 3, 6, 4]
print(maxProfit(n))
