class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
    	"""Array.

    	Running time: O(n^3) where n is the length of arr.
    	"""
        n = len(arr)
        res = 0
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        res += 1
        return res