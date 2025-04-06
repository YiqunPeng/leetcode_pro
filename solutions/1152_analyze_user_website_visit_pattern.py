class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        """Hash table.
        """
        user = collections.defaultdict(list)
        for i in range(len(username)):
            user[username[i]].append((timestamp[i], website[i]))
        
        for k, v in user.items():
            user[k] = sorted(v)

        p = collections.defaultdict(set)
        for u, val in user.items():
            for i in range(len(val)-2):
                for j in range(i+1, len(val)-1):
                    for k in range(j+1, len(val)):
                        p[(val[i][1], val[j][1], val[k][1])].add(u)
        
        res = []
        m = -1
        for w, u in p.items():
            if len(u) > m or (len(u) == m and str(list(w)) < str(res)):
                res = list(w)
                m = len(u)
        return res