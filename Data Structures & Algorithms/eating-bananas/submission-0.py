class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # You eat up to k bananas/hr from that pile
        # which means choose a max of whatever pile has the max number of bananas
        # that's the max k possible
        # to calculate the hours sum(ceil(pile[i]/k)) <= hours
        # k=1, 1/1 + 4/1 + 3/1 + 2/1 = 10, so try with k so on

        # to find the best k, we use binary search among 1 to maxValue
        k = 0
        left = 1
        right = max(piles)
        while left<=right:
            mid = (left + right)//2
            calHrs = 0
            for val in piles:
                calHrs = calHrs + math.ceil(val/mid)
            if calHrs <= h:
                right = mid - 1
                k = mid
            else:
                left = mid + 1

        return k
        