class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        """Hash table.

        Running time: O(n + m) where n is the length of queries and m is the length of wordlist.
        """
        words = set(wordlist)
        lower = {}
        devowel = {}
        res = []
        for w in wordlist[::-1]:
            l = w.lower()
            lower[l] = w
            devowel[re.sub('[aeiou]', '#', l)] = w
        for q in queries:
            lq = q.lower()
            if q in words:
                res.append(q)
            elif lq in lower:
                res.append(lower[lq])
            elif re.sub('[aeiou]', '#', lq) in devowel:
                res.append(devowel[re.sub('[aeiou]', '#', lq)])
            else:
                res.append('')
        return res
