class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        """BFS.

        Running time: O(n) where n is number of processes.
        """
        from collections import defaultdict
        
        d = defaultdict(list)
        for i in range(len(pid)):
            d[ppid[i]].append(pid[i])

        ret = [kill]
        p = 0
        while p < len(ret):
            ret.extend(d[ret[p]])
            p += 1
        
        return ret
