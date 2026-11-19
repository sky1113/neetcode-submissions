from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefCount = Counter(students)
        res = len(students)

        for s in sandwiches:
            if prefCount[s] > 0:
                prefCount[s] -= 1
                res -= 1
            else:
                break
            
        return res
