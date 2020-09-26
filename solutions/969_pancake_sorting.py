class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        """Array.

        Running time: O(n) where n is the length of arr.
        """
        res = []
        n = len(arr)
        for i in range(n, 0, -1):
            pos = arr.index(i)
            if pos == i - 1:
                continue
            res.append(pos + 1)
            res.append(i)
            arr = arr[pos+1:i][::-1] + arr[:pos+1]
        return res
