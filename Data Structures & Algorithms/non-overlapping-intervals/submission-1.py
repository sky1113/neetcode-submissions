class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        if len(intervals) == 1:
            return 0

        prevEnd = intervals[0][1]
        res = 0

        for i in range(1, len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]

            if start < prevEnd:
                prevEnd = min(end, prevEnd)
                res += 1
            else:
                prevEnd = end

        return res
