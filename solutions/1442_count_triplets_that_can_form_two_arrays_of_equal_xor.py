class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        res = 0
        for i in range(len(arr)):
            v = arr[i]
            for j in range(i+1, len(arr)):
                v ^= arr[j]
                if v == 0:
                    res += j - i
        return res
