class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """Topological sort.
        """
        d = collections.defaultdict(set)
        re_d = collections.defaultdict(set)
        for a, b in prerequisites:
            d[a].add(b)
            re_d[b].add(a)
        
        f = 0
        q = collections.deque([])
        for i in range(numCourses):
            if i not in d:
                q.append(i)
                f += 1
        
        while q:
            c = q.popleft()
            for nc in re_d[c]:
                d[nc].remove(c)
                if len(d[nc]) == 0:
                    q.append(nc)
                    f += 1
        
        return f == numCourses