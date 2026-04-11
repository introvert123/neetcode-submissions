class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        profitSum = 0
        left = 0
        right = 1

        while right < len(prices):
            if prices[left] < prices[right]:
                profitSum = profitSum + prices[right] - prices[left]
                left += 1
            else:
                left = right
            right += 1

        
        return profitSum

        


        