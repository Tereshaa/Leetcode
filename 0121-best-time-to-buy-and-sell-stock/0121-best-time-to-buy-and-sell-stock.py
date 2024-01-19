class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n=len(prices)
        profit=0
        minprice=1e4
        for i in range(n):
            if prices[i]<minprice:
                minprice=prices[i]
            profit=max(profit,prices[i]-minprice)
        return profit
                
                
        
        
            
            
        