class WordDistance:

    def __init__(self, words: List[str]):
        """Running Time: O(n) where n is the length of words.
        """
        self.p = collections.defaultdict(list)
        for i, w in enumerate(words):
            self.p[w].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        """Running Time: O(m) where m is the sum of appearance of word1
        and word2 in the original words list.
        """
        l1, l2 = self.p[word1], self.p[word2]
        p1, p2 = 0, 0 
        d = sys.maxsize
        while p1 < len(l1) and p2 < len(l2):
            d = min(d, abs(l1[p1] - l2[p2]))
            if l1[p1] < l2[p2]:
                p1 += 1
            else:
                p2 += 1
        return d
