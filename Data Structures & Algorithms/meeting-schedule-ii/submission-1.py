"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        rooms = 0
        start = []
        end = []

        #whenever we encounter a new start time (meeting started) - it means we need a room
        #if we observe a meeting has ended, it means one room got free
        #max number of rooms needed at any time is the minMeetingrooms

        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)

        start.sort()
        end.sort()

        s,e = 0,0
        count = 0

        while s < len(start) and e < len(end):
            if start[s] < end[e]: #new meeting got started
                count += 1
                s += 1
            else: #meeting got ended before this new one started
                count -= 1
                e += 1
            rooms = max(rooms, count)

        return rooms


        