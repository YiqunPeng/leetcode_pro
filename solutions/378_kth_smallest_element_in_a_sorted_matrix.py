class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        """Heap

        Running time: O(k*n*logn) where n is dimension of matrix. 
        """
        import heapq
        
        n = len(matrix)
        
        heap = []
        for i in range(n):
            heapq.heappush(heap, (matrix[i][0], i, 0))
            
        while k - 1:
            _, r, c = heapq.heappop(heap)
            if c + 1 < n:
                heapq.heappush(heap, (matrix[r][c+1], r, c + 1))
            k -= 1
            
        return heapq.heappop(heap)[0]