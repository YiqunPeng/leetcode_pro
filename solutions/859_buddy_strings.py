class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """String.

        Running time: O(n) where n is the length of A.
        """
        if len(A) != len(B):
            return False
        di = []
        for i in range(len(A)):
            if A[i] != B[i]:
                di.append(i)
                if len(di) > 2:
                    return False
        if len(di) == 2:
            return A[di[0]] == B[di[1]] and A[di[1]] == B[di[0]]
        elif len(di) == 0 and A:
            return max(collections.Counter(A).values()) > 1
        return False