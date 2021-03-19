class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """Hash set.
        """
        rows = [set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']),
                set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']),
                set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])]
        res = []
        for word in words:
            for i in range(3):
                if word[0].lower() in rows[i]:
                    r1 = i
                    break
            for c in word[1:]:
                for i in range(3):
                    if c.lower() in rows[i]:
                        rc = i
                if rc != r1:
                    break
            else:
                res.append(word)
        return res
