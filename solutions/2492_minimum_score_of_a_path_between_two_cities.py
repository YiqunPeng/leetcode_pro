class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        paths = defaultdict(list)
        distances = dict()
        for a, b, d in roads:
            paths[a].append(b)
            paths[b].append(a)
            distances[a] = min(distances[a], d) if a in distances else d
            distances[b] = min(distances[b], d) if b in distances else d
  
        v = set([1])
        q = deque([(1)])
        while q:
            c = q.popleft()
            for nc in paths[c]:
                if nc not in v:
                    v.add(nc)
                    q.append(nc)
        
        res = sys.maxsize
        for c in v:
            res = min(res, distances[c])    
        return res