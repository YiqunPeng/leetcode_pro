class Solution:
    def findLucky(self, arr: List[int]) -> int:
        """Hash table.

        Running time: O(n) where n is the length of arr.
        """
        d = {}
        for a in arr:
            d[a] = d.get(a, 0) + 1
        res = -1
        m = 0
        for k, v in d.items():
            if k == v and k > m:
                res = v
                m = k
        return res
