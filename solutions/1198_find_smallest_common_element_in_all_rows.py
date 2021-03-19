class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        """Array.

        Running time: O(n) where n is the number of items in mat.
        """
        c = collections.defaultdict(int)
        for r in mat:
            for i in r:
                c[i] += 1
        res = None
        for k, v in c.items():
            if v == len(mat) and (not res or k < res):
                res = k
        return res if res else -1
