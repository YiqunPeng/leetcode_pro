class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        """Sort.

        Running time: O(nlogn) where n is the length arr.
        """
        arr.sort()

        m = arr[-1] - arr[0]
        ret = []
        
        for i in range(1, len(arr)):
            if arr[i] - arr[i-1] == m:
                ret.append([arr[i-1], arr[i]])
            elif arr[i] - arr[i-1] < m:
                ret = [[arr[i-1], arr[i]]]
                m = arr[i] - arr[i-1]
        
        return ret
