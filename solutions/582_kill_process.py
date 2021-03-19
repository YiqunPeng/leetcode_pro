class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """BFS.

        Running time: O(n) where n is number of processes.
        """
        d = defaultdict(list)
        for i in range(len(pid)):
            d[ppid[i]].append(pid[i])
        res = []
        q = deque([kill])
        while q:
            p = q.popleft()
            res.append(p)
            q.extend(d[p])
        return res
