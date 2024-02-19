def bestTimeToBuyAndSellStock(prices: [int]) -> int:
    # Write your code here.
    maxPro = 0
    minPrice = float('inf')
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxPro = max(maxPro, prices[i] - minPrice)
    return maxPro
