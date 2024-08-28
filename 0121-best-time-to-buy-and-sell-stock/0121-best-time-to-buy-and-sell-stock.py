class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        n=len(prices)
        maxprofit=0
        while r<n:
            if prices[l]<prices[r]:
                profit=prices[r]-prices[l]
                maxprofit=max(profit,maxprofit)
            else:
                l=r
            r+=1
        return maxprofit


                
                
        
        
            
            
        