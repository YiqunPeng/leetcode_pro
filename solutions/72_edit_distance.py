class Solution:
    
    def __init__(self):
        self.memo = {}
    
    def minDistance(self, word1: str, word2: str) -> int:
        return self._dfs(word1, word2)
    
    def _dfs(self, w1, w2):
        if (w1, w2) in self.memo:
            return self.memo[(w1, w2)]
        if w1 == w2:
            return 0
        if not w1 or not w2:
            return max(len(w1), len(w2))
        if w1[0] == w2[0]:
            res = self._dfs(w1[1:], w2[1:])
        else:
            res = min(self._dfs(w1[1:], w2), self._dfs(w1[1:], w2[1:]), self._dfs(w1, w2[1:])) + 1
        self.memo[(w1, w2)] = res
        return res
