class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        """Array.

        Running time: O(n) where n is the number of items in mat.
        """
        res = []
        rows = set()
        
        p = 0
        while p < len(mat[0]):
            for i in range(len(mat)):
                if i in rows:
                    continue
                if mat[i][p] == 0:
                    res.append(i)
                    rows.add(i)
                    if len(res) == k:
                        return res
            p += 1
        
        i = 0
        while len(res) < k:
            if i not in rows:
                res.append(i)
            i += 1
        
        return res


class Solution1:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = [(sum(mat[i]), i)  for i in range(len(mat))]
        powers.sort(key=lambda x: (x[0], x[1]))
        return [p[1] for p in powers[:k]]
        