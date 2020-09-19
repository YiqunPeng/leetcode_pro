class Solution:
    def isValid(self, S: str) -> bool:
        """Stack.

        Running time: O(n) where n is the length of S.
        """
        s = []
        
        for c in S:
            if c == 'c':
                if len(s) < 2 or s[-2:] != ['a', 'b']:
                    return False
                else:
                    s.pop()
                    s.pop()
            else:
                s.append(c)
                
        return not s