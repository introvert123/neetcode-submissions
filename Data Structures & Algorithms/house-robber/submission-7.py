class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)
        if n == 1:
            return nums[0]

        #we are holding what's the max we could rob up until the ith house
        #remember that we wold have houses that are many numbers apart which could be added, it's not like we rob
        #only alternate houses
        maxRob = [0]*n

        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0],nums[1])

        #either we are going to consider the current element w/o adj or not consider curr element and consider prev
        for i in range(2,n):
            maxRob[i] = max(nums[i] + maxRob[i-2], maxRob[i-1])


        return maxRob[n-1]
        