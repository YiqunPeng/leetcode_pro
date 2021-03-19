class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        x, y = click
        if board[x][y] == 'M':
            board[x][y] = 'X'
            return board
        else:
            self._reveal_blank(board, x, y) 
        return board
    
    def _count_mine(self, board, x, y):
        cnt = 0
        for dx in range(x-1, x+2):
            for dy in range(y-1, y+2):
                if dx == x and dy == y:
                    continue
                if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and board[dx][dy] == 'M':
                    cnt += 1
        return cnt
    
    def _reveal_blank(self, board, x, y):
        q = deque([(x, y)])
        while q:
            x, y = q.popleft()
            if board[x][y] != 'E':
                continue
            cnt = self._count_mine(board, x, y)
            if cnt == 0:
                board[x][y] = 'B'
                for dx in range(x-1, x+2):
                    for dy in range(y-1, y+2):
                        if dx == x and dy == y:
                            continue
                        if 0 <= dx < len(board) and 0 <= dy < len(board[0]) and board[dx][dy] == 'E':
                            q.append((dx, dy))
            else:
                board[x][y] = str(cnt)
