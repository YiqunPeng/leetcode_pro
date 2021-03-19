"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        """BFS.

        Running time: O(n) where n == len(employees).
        """
        res = 0
        s = {}
        v = {}
        for e in employees:
            s[e.id] = e.subordinates
            v[e.id] = e.importance
        q = collections.deque([id])
        while q:
            i = q.popleft()
            res += v[i]
            for sub in s[i]:
                q.append(sub)
        return res
