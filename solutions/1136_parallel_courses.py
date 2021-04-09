class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        dep = defaultdict(set)
        pre = defaultdict(set)
        for a, b in relations:
            dep[a].add(b)
            pre[b].add(a)
        res = 0
        q = deque()
        for i in range(1, n + 1):
            if len(dep[i]) == 0:
                q.append(i)
        while q:
            nxt = deque()
            for i in range(len(q)):
                c = q.popleft()
                for p in pre[c]:
                    dep[p].remove(c)
                    if len(dep[p]) == 0:
                        nxt.append(p)
            q = nxt
            res += 1
        if all(len(v) == 0 for v in dep.values()):
            return res
        else:
            return -1
