
# O(n) and O(1) space


def bestBuy(prices):
    maxProfit = 0
    if prices is not None:
        minBuy = prices[0]
        for price in range(len(prices) - 1):
            checkProfit = prices[price + 1] - minBuy
            if checkProfit < 0:
                minBuy = prices[price]
            else:
                if checkProfit > maxProfit:
                    maxProfit = checkProfit

    return maxProfit


def bestTime(prices):
    maxProfit = 0
    minBuy = float("inf")

    for price in prices:
        minBuy = min(minBuy, price)
        minProfit_to_sell = price - minBuy
        maxProfit = max(maxProfit, minProfit_to_sell)

    return maxProfit


print(bestTime([7, 1, 5, 3, 6, 4]))
