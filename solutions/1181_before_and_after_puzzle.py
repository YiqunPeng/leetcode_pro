class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        """String.
        """
        s = collections.defaultdict(set)
        e = collections.defaultdict(set)
        for i, p in enumerate(phrases):
            words = p.split(' ')
            e[words[0]].add(i)
            s[words[-1]].add(i)
        res = set()
        for k, v in e.items():
            if k in s:
                for i in v:
                    for j in s[k]:
                        if i != j:
                            ew = phrases[i].split(' ')
                            if len(ew) == 1:
                                res.add(phrases[j])
                            else:
                                res.add(phrases[j] + ' ' + ' '.join(ew[1:]))
        return sorted(res)
