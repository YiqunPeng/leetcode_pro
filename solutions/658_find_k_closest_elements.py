class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        """Binary search.

        Running time: O(nlogn) where n is the length of arr.
        """
        if x <= arr[0]:
            return arr[:k]
        if x >= arr[-1]:
            return arr[-k:]
        
        res = collections.deque()
        
        l, r = 0, len(arr)
        p = -1
        while l < r:
            m = l + (r - l) // 2
            if arr[m] <= x < arr[m + 1]:
                p = m
                break
            elif arr[m] > x:
                r = m
            else:
                l = m
        
        l, r = p, p + 1
        while len(res) < k:
            if l < 0:
                res.append(arr[r])
                r += 1
            elif r >= len(arr):
                res.appendleft(arr[l])
                l -= 1
            elif x - arr[l] > arr[r] - x:
                res.append(arr[r])
                r += 1
            else:
                res.appendleft(arr[l])
                l -= 1
        
        return res
                