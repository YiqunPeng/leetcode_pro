class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        """Hash table.

        Running time: O(n) where n == len(cpdomains).
        """
        d = collections.defaultdict(int)
        for cpdomain in cpdomains:
            s = cpdomain.split(' ')
            lvls = s[1].split('.')
            domain = lvls[-1]
            d[domain] += int(s[0])
            for i in range(len(lvls) - 2, -1, -1):
                domain = lvls[i] + '.' + domain
                d[domain] += int(s[0])
        return [str(v) + ' ' + k for k, v in d.items()] 
