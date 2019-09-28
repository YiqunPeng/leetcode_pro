class Solution:
    def numberOfLines(self, widths: List[int], S: str) -> List[int]:
        """Math.

        Running time: O(n) where n is the length of S.
        """
        l, w = 0, 0
        
        for c in S:
            cw = widths[ord(c) - ord('a')]
            
            if w + cw > 100:
                l += 1
                w = cw
            else:
                w += cw
                
        return l + 1, w