class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        """Two pointers.

        Running time: O(n) where n is the length of S.
        """
        l, r = 0, 1
        res = []
        
        while r < len(S):
            if S[l] != S[r]:
                if r - l >= 3:
                    res.append([l, r - 1])
                l = r
            r += 1
                
        if r - l >= 3:
            res.append([l, r - 1])
        
        return res
        