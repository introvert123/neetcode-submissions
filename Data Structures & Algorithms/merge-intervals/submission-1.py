class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        res = []

        res.append(intervals[0])
        k = 0
        for i in range(1,len(intervals)):
            if res[k][1] >= intervals[i][0]: #overlapping
                element = res.pop()
                res.append([min(element[0],intervals[i][0]),max(element[1],intervals[i][1])])
            else:
                res.append(intervals[i])
                k += 1
        return res
        