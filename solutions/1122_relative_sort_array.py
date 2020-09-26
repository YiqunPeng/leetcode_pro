class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """Hash table.

        Running time: O(nlogn) where n is the length of arr1.
        """
        s = set(arr2)
        f = {}
        ex = []
        for a in arr1:
            if a in s:
                f[a] = f.get(a, 0) + 1
            else:
                ex.append(a)
        res = []
        for a in arr2:
            if a in f:
                res.extend([a] * f[a])
        return res + sorted(ex)
