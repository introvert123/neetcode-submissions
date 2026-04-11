class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        n = len(prices)
        left = 0 # buy
        right = left + 1 #sell
        maxValue = 0
        while right < n:
            if prices[left] > prices[right]:
                # we have found a better lower price to buy at right
                # so we make our buy position to right
                left = right
            else:
                maxValue = max(prices[right] - prices[left], maxValue)
            right = right + 1

        return maxValue    