class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        v = set()
        res = 0
        for i in range(n):
            if i not in v:
                res += 1
                v.add(i)
                self._bfs(isConnected, v, i)
        return res
    
    def _bfs(self, c, v, i):
        q = deque([i])
        while q:
            city = q.popleft()
            for j in range(len(c)):
                if c[city][j] == 1 and j not in v:
                    v.add(j)
                    q.append(j)
