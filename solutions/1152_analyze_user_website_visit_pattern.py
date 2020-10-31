class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        p = collections.defaultdict(list)
        for i in range(len(username)):
            p[username[i]].append((timestamp[i], website[i]))
        for k, v in p.items():
            v.sort(key=lambda x: x[0])
        f = collections.defaultdict(set)
        for k, v in p.items():
            for a in range(len(v) - 2):
                for b in range(a + 1, len(v) - 1):
                    for c in range(b + 1, len(v)):
                        f[tuple([v[a][1], v[b][1], v[c][1]])].add(k)
        m = -1
        res = tuple()
        for k, v in f.items():
            if len(v) > m or (len(v) == m and self._compare(k, res)):
                res = k
                m = len(v)
        return list(res)
    
    def _compare(self, t1, t2):
        if not t2:
            return True
        if t1[0] != t2[0]:
            return t1[0] < t2[0]
        elif t1[1] != t2[1]:
            return t1[1] < t2[1]
        else:
            return t1[2] < t2[2]
