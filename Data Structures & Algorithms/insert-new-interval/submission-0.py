class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = list()

        start, end = newInterval[0], newInterval[1]

        for i in range(len(intervals)):
            a, b = intervals[i][0], intervals[i][1]
            # no overlap, entire interval before new
            if b < start:
                result.append([a, b])
            # could have overlap
            if b >= start:
                # entire interval after new interval
                if a > end:
                    result.append([start, end])
                    result.extend(intervals[i::])
                    return result
                # there's some overlap
                else:
                    start = min(start, a)
                    end = max(end, b)

        result.append([start, end])
        return result