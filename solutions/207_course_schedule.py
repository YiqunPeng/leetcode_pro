class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prer = defaultdict(set)
        inde = {}
        for a, b in prerequisites:
            prer[b].add(a)
            inde[b] = inde.get(b, 0)
            inde[a] = inde.get(a, 0) + 1
        q = deque()
        for k in inde:
            if inde[k] == 0:
                q.append(k)
        while q:
            node = q.popleft()
            for c in prer[node]:
                inde[c] -= 1
                if inde[c] == 0:
                    q.append(c)
        return all(inde[k] == 0 for k in inde)
