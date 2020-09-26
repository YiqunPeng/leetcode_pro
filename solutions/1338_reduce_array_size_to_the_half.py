from collections import Counter

class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        """Hash table.

        Running time: O(nlogn) where n is the length of arr.
        """
        n = len(arr)
        c = Counter(arr)
        f = sorted(c.values())
        res = 0
        s = 0
        while s < n // 2:
            s += f.pop()
            res += 1
        return res
