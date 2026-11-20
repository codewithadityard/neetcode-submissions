class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        result=0
        for i in range(1,len(prices)):
            sell=prices[i]
            profit=sell-buy
            if profit <= 0:
                buy=prices[i]
            result=max(result,profit)

        return result
            
            


        