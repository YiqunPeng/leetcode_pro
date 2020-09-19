class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """BFS.
        
        Running time: O(k) where k is the number of rooms.
        """
        INF = 2 ** 31 - 1
        
        q = collections.deque()
        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j, 0))
                    
        while q:
            i, j, d = q.popleft()
            
            for ni, nj in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= ni < len(rooms) and 0 <= nj < len(rooms[0]) and rooms[ni][nj] == INF:
                    rooms[ni][nj] = d + 1
                    q.append((ni, nj, d + 1))
        