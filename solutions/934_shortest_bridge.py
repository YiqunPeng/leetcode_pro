class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        """DFS/BFS.

        Running Time: O(n) where n is the number of grids in A.
        """
        from collections import deque
        
        def find_start():
            for i in range(len(A)):
                for j in range(len(A[0])):
                    if A[i][j] == 1:
                        return i, j
                    
        def populate(i, j, outliner):
            A[i][j] = 2
            
            for ni, nj in [(i+1, j), (i-1, j), (i, j-1), (i, j+1)]:
                if 0 <= ni < len(A) and 0 <= nj < len(A[0]):
                    if A[ni][nj] == 1:
                        populate(ni, nj, outliner)
                    if A[ni][nj] == 0:
                        outliner.add((i, j))
                    
        si, sj = find_start()
        outliner = set()
        populate(si, sj, outliner)
        
        v = set()
        q = deque()
        for i, j in outliner:
            q.append((i, j, 0))
        
        while q:
            i, j, n = q.popleft()
            
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < len(A) and 0 <= nj < len(A[0]) and A[ni][nj] != 2:
                    if A[ni][nj] == 1:
                        return n
                    if (ni, nj) not in v:
                        v.add((ni, nj))
                        q.append((ni, nj, n + 1))
   