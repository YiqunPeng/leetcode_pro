class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        """Hash table. Sort.

        Running time: O(nlogn) where n == len(A).
        """
        c = collections.Counter(A)
        keys = sorted(c.keys())
        for i, key in enumerate(keys):
            if c[key] == 0:
                continue
            if key == 0:
                if c[key] % 2 == 1:
                    return False
            elif key < 0:
                if key % 2 == 1 or key // 2 not in c or c[key//2] < c[key]:
                    return False
                else:
                    c[key // 2] -= c[key]
            else:
                if key * 2 not in c or c[key * 2] < c[key]:
                    return False
                else:
                    c[key * 2] -= c[key]              
        return True
