class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        road = {0}
        q = deque(connections)
        res = 0
        while q:
            a, b = q.popleft()
            if a in road:
                res += 1
                road.add(b)
            elif b in road:
                road.add(a)
            else:
                q.append([a, b])
        return res
