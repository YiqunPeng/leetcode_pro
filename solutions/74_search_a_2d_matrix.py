class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """Binary Search.

        Running time: O(logr + logc) where r is the number of rows and c is the numebr of columns.
        """
        def search_row(arr):
            if target <= arr[0]:
                return 0
            if target > arr[-1]:
                return -1
            l, r = 0, len(arr)
            while l < r:
                m = l + (r - l) // 2
                if arr[m] == target or (m > 0 and arr[m - 1] < target <= arr[m]):
                    return m
                elif arr[m] > target:
                    r = m
                else:
                    l = m
               
        def search_value(arr):
            if target < arr[0] or target > arr[-1]:
                return -1
            l, r = 0, len(arr)
            while l < r:
                m = l + (r - l) // 2
                if arr[m] == target:
                    return m
                elif arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return -1
        
        if not matrix or not matrix[0]:
            return False
        
        r = search_row([i[-1] for i in matrix])
        if r == -1:
            return False
        
        c = search_value(matrix[r])
        return c != -1          
        