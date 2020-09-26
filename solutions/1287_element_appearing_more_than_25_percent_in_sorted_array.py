class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
    	"""Array.

    	Running time: O(nlogn) where n is the length of arr.
    	"""
        n = len(arr)
        for i in [n // 4, n // 2, n * 3 // 4]:
            f = self._first_apperance(arr[:i+1], arr[i])
            l = self._last_apperance(arr[i:], arr[i]) + i
            if l - f + 1 > n // 4:
                return arr[i]
        
    def _first_apperance(self, a, v):
        l, r = 0, len(a)
        while l < r:
            m = (l + r) // 2
            if a[m] == v and (m == 0 or a[m-1] != v):
                return m
            elif a[m] >= v:
                r = m
            else:
                l = m + 1
                
    def _last_apperance(self, a, v):
        l, r = 0, len(a)
        while l < r:
            m = (l + r) // 2
            if a[m] == v and (m == len(a) - 1 or a[m+1] != v):
                return m
            elif a[m] > v:
                r = m
            else:
                l = m + 1
