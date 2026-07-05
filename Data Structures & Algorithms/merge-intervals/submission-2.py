class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        res = []

        res.append(intervals[0])
        for i in range(1,len(intervals)):
            if res[-1][1] >= intervals[i][0]: #overlapping
                res[-1][1] = max(res[-1][1], intervals[i][1]) #only max element changes as min start is in res
            else:
                res.append(intervals[i])
        return res
        