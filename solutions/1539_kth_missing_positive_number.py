class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        if k < arr[0]:
            return k
        k -= arr[0] - 1
        p = 1
        while k > 0 and p < len(arr):
            di = arr[p] - arr[p-1] - 1
            if di >= k:
                return k + arr[p-1]
            k -= di
            p += 1
        return arr[-1] + k
