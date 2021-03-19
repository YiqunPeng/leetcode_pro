class Solution:
    
    def __init__(self):
        self.seen = set()
    
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        """DFS.
        """
        if start == destination:
            return True
        self.seen.add(tuple(start))
        m, n = len(maze), len(maze[0])
        res = False
        for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            x, y = start[0], start[1]
            while 0 <= x + dx < m and 0 <= y + dy < n and maze[x+dx][y+dy] == 0:
                x += dx
                y += dy
            if (x, y) not in self.seen:
                res = res or self.hasPath(maze, [x, y], destination)
            if res:
                return True
        return False
