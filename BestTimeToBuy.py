
# O(n) and O(1) space

def bestBuy(prices):
    maxProfit = 0
    if prices is not None:
        minBuy = prices[0]
        for price in range(len(prices) - 1):
            checkProfit = prices[price + 1] - minBuy
            if checkProfit < 0:
                minBuy = prices[price+1]
            else:
                if checkProfit > maxProfit:
                    maxProfit = checkProfit
        
    return maxProfit
                
print(bestBuy([7, 1, 5, 3, 6, 4]))