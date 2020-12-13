class Solution:
    def boldWords(self, dict: List[str], s: str) -> str:
        """String.
        """
        intervals = []
        for i in range(len(s)):
            for w in dict:
                if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                    intervals.append([i, i + len(w)])
        if not intervals:
            return s
        merge = []
        for l, r in intervals:
            if not merge or l > merge[-1][1]:
                merge.append([l, r])
            else:
                merge[-1][1] = max(merge[-1][1], r)
        res = [s[:merge[0][0]]]
        for i in range(len(merge)):
            l, r = merge[i][0], merge[i][1]
            res.append(s[merge[i-1][1]:l])
            res.append('<b>' + s[l:r] + '</b>')
        return ''.join(res + [s[merge[-1][1]:]])
