class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        """String.

        Running time: O(n) where n is the length of A.
        """
        if len(A) != len(B) or len(A) < 2:
            return False
        
        diff = []
        c = collections.defaultdict(int)
        for i in range(len(A)):
            c[A[i]] += 1
            if A[i] != B[i]:
                if len(diff) == 2:
                    return False
                else:
                    diff.append(i)
        
        if len(diff) == 2:
            return A[diff[0]] == B[diff[1]] and A[diff[1]] == B[diff[0]]
        elif len(diff) == 0:
            return min(c.values()) >= 2
        else:
            return False