class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 10000
        result = 0

        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            result = max(result, prices[i]-min_price)

        return result