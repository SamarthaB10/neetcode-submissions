class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        c,m = (0,0)
        for x in range(len(prices)-1): 
            j = x + 1
            while j < len(prices): 
                if prices[j] < prices[x]:
                    j+=1 
                    continue 
                c = prices[j] - prices[x]
                m = max(c,m)
                j+=1
        return(m)

            




'''
[10,1,5,6,7,1]
maxProfit = 0 
currProfit = 


(0,10)
(1,1)


'''