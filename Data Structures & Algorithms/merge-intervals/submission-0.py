class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        if len(intervals) == 1:
            return intervals

        res = list()

        s1, e1 = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            s2, e2 = intervals[i][0], intervals[i][1]

            print([s1, e1], [s2, e2])
            
            # overlap
            if s2 <= e1:
                s1 = min(s1, s2)
                e1 = max(e1, e2)
            else:
                res.append([s1, e1])
                s1 = s2
                e1 = e2
        
        res.append([s1, e1])
        return res
    
