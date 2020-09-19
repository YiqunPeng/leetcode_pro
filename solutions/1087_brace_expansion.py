class Solution:
    def expand(self, S: str) -> List[str]:
        """Backtracking.

        Running time: O(k) where k is the length of result.
        """
        def backtracking(res, word, l):
            if not l:
                res.append(word)
            else:
                for c in l[0]:
                    res = backtracking(res, word + c, l[1:])
            return res
        
        letters = []
        
        l, r = 0, 0
        while r < len(S):
            if S[r] == '{':
                l = r + 1
                while S[r] != '}':
                    r += 1
                letters.append(S[l:r].split(','))
            else:
                letters.append([S[r]])
            r += 1
        
        return sorted(backtracking([], '', letters))