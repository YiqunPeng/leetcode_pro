class Solution:
    def countArrangement(self, N: int) -> int:
        """Backtracking.

        Running time: O(N!)
        """
        def backtracking(i, visited):
            res = 0           
            for num in arr[i]:
                if num not in visited:
                    if i == N:
                        res += 1
                    else:
                        visited.add(num)
                        res += backtracking(i + 1, visited)
                        visited.remove(num)        
            return res
               
        arr = {}
        for i in range(1, N + 1):
            arr[i] = set([j for j in range(1, N + 1) if i % j == 0 or j % i == 0])
        
        return backtracking(1, set())