class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        """Array.

        Running time: O(n) where n is the length of moves.
        """
        n = len(moves)
        ac = [0, 0, 0, 0, 0, 0, 0, 0]
        bc = [0, 0, 0, 0, 0, 0, 0, 0]        
        
        for i in range(n):
            r, c = moves[i]
            if i % 2 == 0:
                self._update(ac, r, c)
            else:
                self._update(bc, r, c)

        if n % 2 == 1: 
            if any(i == 3 for i in ac):
                return 'A'
        else:
            if any(i == 3 for i in bc):
                return 'B'

        return 'Draw' if len(moves) == 9 else 'Pending'
               
    def _update(self, p, r, c):
        p[r] += 1
        p[c+3] += 1
        if r == c:
            p[6] += 1
        if r + c == 2:
            p[7] += 1
