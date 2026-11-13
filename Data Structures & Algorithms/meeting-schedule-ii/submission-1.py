"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        rooms  = 0
        maxrooms = 0
        start = sorted([s.start for s in intervals])
        end = sorted([e.end for e in intervals])
        j= i= 0
        while i < len(intervals):
            if start[i] < end[j]:
                rooms+=1
                i+=1
                maxrooms = max(rooms, maxrooms)
            else:
                j+=1
                rooms -=1
        return maxrooms 
                



        