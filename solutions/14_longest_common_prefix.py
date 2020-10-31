class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """String.
        """
        if not strs:
            return ""
        p = 0
        while p < len(strs[0]):
            for s in strs:
                if p == len(s) or s[p] != strs[0][p]:
                    return strs[0][:p]
            p += 1
        return strs[0][:p]
