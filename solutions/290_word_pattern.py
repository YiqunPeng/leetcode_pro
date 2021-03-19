class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        """Hash table.
        """
        sp, ps = {}, {}
        words = s.split(' ')
        if len(words) != len(pattern):
            return False
        for i, p in enumerate(pattern):
            if p not in ps:
                ps[p] = words[i]
            elif ps[p] != words[i]:
                return False
            if words[i] not in sp:
                sp[words[i]] = p
            elif sp[words[i]] != p:
                return False
        return True
