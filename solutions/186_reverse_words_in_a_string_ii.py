class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """Two pointers.

        Running time: O(n) where n is the length of s.
        """
        l, r = 0, 0
        
        while r < len(s):
            if s[r] != ' ':
                r += 1
            else:
                t = r + 1
                r -= 1
                while l < r:
                    s[l], s[r] = s[r], s[l]
                    l += 1
                    r -= 1
                l = r = t
            
        r -= 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        s[:] = s[::-1]
