class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0 
        minprice = prices[0]

        for r in range(len(prices)): 
            minprice = min(minprice,prices[r])

            curProfit = prices[r] - minprice

            maxProfit = max(maxProfit,curProfit)

        return maxProfit



