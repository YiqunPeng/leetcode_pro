class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.

        Running time: O(n) where n is the length of arr.
        """
        n = len(arr)
        c = 0
        for i in arr:
            if i == 0:
                c += 1
        j = n + c - 1
        for i in range(n - 1, -1, -1):
            if arr[i] != 0:
                if j < n:
                    arr[j] = arr[i]
                j -= 1
            else:
                if j < n:
                    arr[j] = 0
                j -= 1
                if j < n:
                    arr[j] = 0
                j -= 1
