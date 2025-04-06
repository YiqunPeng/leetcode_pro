class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """Topological sort.
        """
        d = collections.defaultdict(int)
        rev_d = collections.defaultdict(set)
        for a, b in prerequisites:
            d[a] += 1
            rev_d[b].add(a)
        
        res = []
        q = collections.deque([])
        for i in range(numCourses):
            if d[i] == 0:
                q.append(i)
                res.append(i)
        
        while q:
            c = q.popleft()
            for nc in rev_d[c]:
                d[nc] -= 1
                if d[nc] == 0:
                    q.append(nc)
                    res.append(nc)
        
        return res if len(res) == numCourses else []