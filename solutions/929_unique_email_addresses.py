class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        """String.

        Running time: O(n) where n == len(emails).
        """
        s = set()
        for e in emails:
            s.add(self._santize(e))
        return len(s)
    
    def _santize(self, e):
        p = e.split('@')
        l, d = p[0], p[1]
        s = l.split('+')[0]
        return s.replace('.', '') + '@' + d
