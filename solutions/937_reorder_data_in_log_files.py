class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """String.

        Running time: O(nlogn) where n is the number of logs.
        """
        l, d = [], []
        for log in logs:
            i, w = log.split(' ', 1)
            if 'a' <= w[0] <= 'z':
                l.append((w, i))
            else:
                d.append(log)
        l.sort()
        return [i[1] + ' ' + i[0] for i in l] + d