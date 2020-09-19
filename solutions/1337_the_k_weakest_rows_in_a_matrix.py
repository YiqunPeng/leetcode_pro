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