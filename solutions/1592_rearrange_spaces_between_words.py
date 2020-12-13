class Solution:
    def reorderSpaces(self, text: str) -> str:
        """String.

        Running time: O(n) where n == len(text).
        """
        words = []
        w = ''
        s = 0
        for i in text:
            if i == ' ':
                s += 1
                if w:
                    words.append(w)
                    w = ''
            else:
                w += i
        if w:
            words.append(w)
        if len(words) > 1:
            d, m = divmod(s, len(words) - 1)
        else:
            d, m = 0, s
        sep = ' ' * d
        return sep.join(words) + ' ' * m
