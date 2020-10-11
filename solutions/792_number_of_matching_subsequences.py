class Solution:
    def numMatchingSubseq(self, S: str, words: List[str]) -> int:
        """Array.

        Running time: O(s + w) where s == len(S) and w == sum(length of each word in words).
        """
        n = len(words)
        d = collections.defaultdict(list)
        for word in words:
            d[word[0]].append(iter(word[1:]))
        res = 0
        for s in S:
            iters = d.pop(s, [])
            for i in iters:
                d[next(i, "")].append(i)
        return len(d[""])
