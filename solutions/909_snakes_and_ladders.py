class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        """BFS.
        """
        if not board:
            return 0 
        n = len(board)
        d = self._map_numbers(n, board)
        q = deque([(1, 0)])
        v = set([1])
        while q:
            i, s = q.popleft()
            if i == n * n:
                return s
            for dice in range(1, 7):
                ni = i + dice
                if ni > n * n:
                    break
                if d[ni] != -1:
                    ni = d[ni]
                if ni not in v:
                    v.add(ni)
                    q.append((ni, s+1))
        return -1
    
    def _map_numbers(self, n, board):
        d = {}
        v = 1
        for i in range(n - 1, -1, -1):
            if (n - 1 - i) % 2 == 0:
                for j in range(n):
                    d[v] = board[i][j]
                    v += 1
            else:
                for j in range(n - 1, -1, -1):
                    d[v] = board[i][j]
                    v += 1
        return d
