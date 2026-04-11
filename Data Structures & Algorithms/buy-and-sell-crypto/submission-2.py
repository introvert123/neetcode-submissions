class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        left = 0
        right = 1
        profit = 0

        while left < right and right < n:
            if prices[right] > prices[left]:
                profit = max(profit, prices[right] - prices[left])
                right += 1
            else:
                left = right
                right += 1


        return profit
        