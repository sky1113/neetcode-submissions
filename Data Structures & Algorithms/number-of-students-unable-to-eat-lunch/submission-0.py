from collections import deque, Counter

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        prefCount = Counter(students)
        q = deque(students)
        s = deque(sandwiches)

        while s and prefCount[s[0]] > 0:
            if q[0] == s[0]:
                prefCount[q[0]] -= 1
                q.popleft()
                s.popleft()
            else:
                q.rotate(-1)

        return len(q)
