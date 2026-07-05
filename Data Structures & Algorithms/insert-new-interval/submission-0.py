class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        #three cases
        #either the new interval exists to the entire left of the intervals (beginning)
        #either it is somewhere in between without overlapping any
        #if overlapping we merge


        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:] # adding all the intervals to res after newInterval
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [min(intervals[i][0],newInterval[0]),max(intervals[i][1],newInterval[1])]

        res.append(newInterval)
        return res

        