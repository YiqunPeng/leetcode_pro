class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        """Hash table.

        Running time: O(nlogn) where n is the length of arr.
        """
        c = collections.Counter(arr)
        f = sorted(c.values(), reverse=True)
        while k > 0:
            if k >= f[-1]:
                k -= f[-1]
                f.pop()
            else:
                break
        return len(f)
