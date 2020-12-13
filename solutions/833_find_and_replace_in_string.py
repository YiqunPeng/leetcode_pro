class Solution:
    def findReplaceString(self, S: str, indexes: List[int], sources: List[str], targets: List[str]) -> str:
        """String.

        Running time: O(n*s) where s == len(S) and n == len(indexes).
        """
        l = list(S)
        for i in range(len(indexes)):
            idx = indexes[i]
            s = sources[i]
            t = targets[i]
            if S[idx:idx+len(s)] == s:
                l[idx] = t
                for j in range(idx+1, idx+len(s)):
                    l[j] = ''
        return ''.join(l)
