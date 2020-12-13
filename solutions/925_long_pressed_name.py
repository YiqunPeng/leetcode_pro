class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        """String.

        Running time: O(n) where n is the length of typed.
        """
        n = self._run_length(name)
        t = self._run_length(typed)
        if len(n) != len(t):
            return False
        for i in range(len(n)):
            if n[i][0] != t[i][0] or n[i][1] > t[i][1]:
                return False
        return True
    
    def _run_length(self, arr):
        res = []
        c = 1
        for i in range(1, len(arr)):
            if arr[i] != arr[i-1]:
                res.append((arr[i-1], c))
                c = 1
            else:
                c += 1
        res.append((arr[-1], c))
        return res

