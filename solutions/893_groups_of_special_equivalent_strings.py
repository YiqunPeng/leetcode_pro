class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        """String.

        Running time: O(n) where n is the length of A.
        """
        def get_hash(s):
            e, o = '', ''
            for i in range(len(s)):
                if i % 2:
                    o += s[i]
                else:
                    e += s[i]
            return ''.join(sorted(e) + sorted(o))
        
        return len(set([get_hash(a) for a in A]))
