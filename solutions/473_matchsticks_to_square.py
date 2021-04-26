class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        l = sum(matchsticks)
        if l % 4 != 0:
            return False
        size = l // 4
        matchsticks.sort()
        return self._dfs(matchsticks, len(matchsticks)-1, [size] * 4)
    
    def _dfs(self, ms, pos, sizes):
        if pos == -1:
            return sum(sizes) == 0
        for i in range(4):
            if sizes[i] < ms[pos]:
                continue
            sizes[i] -= ms[pos]
            if self._dfs(ms, pos - 1, sizes):
                return True
            sizes[i] += ms[pos]
        return False
