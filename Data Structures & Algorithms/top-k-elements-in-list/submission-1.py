class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        map = {}
        n = len(nums)
        res = []
        arr = [[] for i in range(n + 1)]

        for val in nums:
            map[val] = map.get(val,0) + 1

        for num, cnt in map.items():
            arr[cnt].append(num)

        i = n
        while i>0:
            for val in arr[i]:
                res.append(val)
                if k == len(res):
                    return res
            i -= 1
        
        return res
        