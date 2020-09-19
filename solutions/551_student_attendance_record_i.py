class Solution:
    def checkRecord(self, s: str) -> bool: 
        """Array.

        Running time: O(n) where n is the length of s.
        """
        a = 0
        l = 0
        
        for c in s:
            if c == 'A':
                a += 1
                if a > 1:
                    return False
                l = 0
            elif c == 'L':
                l += 1
                if l > 2:
                    return False
            else:
                l = 0
                
        return True