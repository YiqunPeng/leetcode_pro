class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        g = defaultdict(set)
        inde = defaultdict(int)
        for a, b in prerequisites:
            g[b].add(a)
            inde[a] += 1
        q = deque()
        res = []
        for i in range(numCourses):
            if inde[i] == 0:
                res.append(i)
                q.append(i)
        while q:
            node = q.popleft()
            for cour in g[node]:
                inde[cour] -= 1
                if inde[cour] == 0:
                    res.append(cour)
                    q.append(cour)
        if len(res) == numCourses:
            return res
        else:
            return []
