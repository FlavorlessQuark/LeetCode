class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = prices[0]
        profit = 0
        
        size = len(prices)
        for x in range(size):
            low = min(low, prices[x])
            profit = max(profit, prices[x] - low)
            # print(f"Profit {profit} high {low}  current {x} {prices[x]}")
        return profit
