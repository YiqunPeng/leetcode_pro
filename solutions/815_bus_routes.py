class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        """BFS.
        """
        d = defaultdict(list)
        for i in range(len(routes)):
            for stop in routes[i]:
                d[stop].append(i)
        q = deque([(source, 0)])
        v = set()
        while q:
            stop, s = q.popleft()
            if stop == target:
                return s
            for bus in d[stop]:
                if bus not in v:
                    v.add(bus)
                    for route in routes[bus]:
                        q.append((route, s + 1))
        return -1
