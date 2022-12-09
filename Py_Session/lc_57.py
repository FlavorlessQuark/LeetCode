class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not len(intervals):
            return [newInterval]

        i = 0
        if (intervals[0][0] >= newInterval[0]):
            intervals.insert(0, newInterval)
        else:
            while (i < len(intervals) - 1):
                if (intervals[i][0] <= newInterval[0] and intervals[i + 1][0] >= newInterval[0]):
                    print(intervals[i])
                    break 
                i += 1
            intervals.insert(i + 1, newInterval)
        print(intervals)
        while (i + 1 < len(intervals)):
            if (intervals[i][1] >= intervals[i + 1][0]):
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                intervals[i][0] = min(intervals[i][0], intervals[i + 1][0])
                del intervals[i + 1]
                i -= 1
            i += 1
        return intervals
