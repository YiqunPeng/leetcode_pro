class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        """Array.

        Running time: O(n + m) where n is the length of A and m is the length of queries.
        """
        ans = []
        s = sum([i for i in A if i % 2 == 0])
        for v, i in queries:           
            if A[i] % 2 == 0 and (A[i] + v) % 2 == 1:
                s = s - A[i]
            elif A[i] % 2 == 1 and (A[i] + v) % 2 == 0:
                s = s + A[i] + v
            elif A[i] % 2 == 0 and (A[i] + v) % 2 == 0:
                s = s + v
            A[i] += v
            ans.append(s)
        return ans
