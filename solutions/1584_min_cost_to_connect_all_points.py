class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        used = set()
        all_d = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                all_d.append((i, j, d))
        all_d.sort(key=lambda x:x[2])
        used.add(all_d[0][0])
        used.add(all_d[0][1])
        res = all_d[0][2]
        all_d.pop(0)
        while len(used) < n:
            p = 0
            while p < len(all_d):
                if all_d[p][0] in used and all_d[p][1] in used:
                    p += 1
                    continue
                if all_d[p][0] in used or all_d[p][1] in used:
                    break
                p += 1
            used.add(all_d[p][0])
            used.add(all_d[p][1])
            res += all_d[p][2]
            all_d.pop(p)
        return res
