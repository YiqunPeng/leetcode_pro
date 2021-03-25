class Solution:
    def spiralMatrixIII(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = [(r0, c0)]
        step = 1
        while len(res) < R * C:
            # right
            for j in range(step):
                c0 += 1
                if self._in_grid(c0, r0, C, R):
                    res.append((r0, c0))
            # down
            for i in range(step):
                r0 += 1
                if self._in_grid(c0, r0, C, R):
                    res.append((r0, c0)) 
            step += 1
            # left
            for j in range(step):
                c0 -= 1
                if self._in_grid(c0, r0, C, R):
                    res.append((r0, c0))           
            # up
            for i in range(step):
                r0 -= 1
                if self._in_grid(c0, r0, C, R):
                    res.append((r0, c0))   
            step += 1
        return res
    
    def _in_grid(self, c0, r0, C, R):
        return 0 <= c0 < C and 0 <= r0 < R
