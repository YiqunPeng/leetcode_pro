class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        """Hash table.

        Running time: O(n) where n == len(arr).
        """
        d = collections.defaultdict(int)
        for a in arr:
            d[a % k] += 1
        for key, v in d.items():
            if key == 0 and v % 2 == 1:
                return False
            elif key != 0 and v != d[k - key]:
                return False
        return True
