class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        tree = defaultdict(set)
        for i in range(len(manager)):
            tree[manager[i]].add(i)
        return self._dfs(headID, informTime, tree)
    
    def _dfs(self, head, time, tree):
        res = 0
        for emp in tree[head]:
            res = max(res, self._dfs(emp, time, tree))
        return res + time[head]
