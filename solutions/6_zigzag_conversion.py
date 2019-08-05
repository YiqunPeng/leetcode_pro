class Solution:
    def convert(self, s: str, numRows: int) -> str:
        """Array

        Running Time: O(n) where n is the length of s.
        """
        rows = ['' for row in range(numRows)]
        
        r = 0
        down = True
        
        for c in s:
            rows[r] += c
            
            if down:
                r += 1
                if r == numRows:
                    r = max(r - 2, 0)
                    down = False
            else:
                r -= 1
                if r == -1:
                    r = min(r + 2, numRows - 1)
                    down = True
        
        return ''.join(rows)
 