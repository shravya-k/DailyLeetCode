class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        high=0
        for i in range(len(prices)-1):
            minpr=prices[i]
            maxpr=max(prices[i+1:])
            if high<(maxpr-minpr):
                high=maxpr-minpr
            
        if high>=0:
            return high
        return 0
            
            
            
            
        
