class Solution:
    def entityParser(self, text: str) -> str:
        """String.

        Running time: O(n) where n == len(text).
        """
        d = {'&quot;': '\"', '&apos;': '\'', '&amp;': '&', '&gt;': '>', '&lt;': '<', '&frasl;': '/'}
        l, r = 0, 0
        while l < len(text):
            if text[l] == '&':
                r = text.find(';', l) + 1
                e = text[l:r]
                if e in d:
                    text = text[:l] + d[e] + text[r:]
                    l += 1
                else:
                    l = r
            else:
                l += 1
        return text
