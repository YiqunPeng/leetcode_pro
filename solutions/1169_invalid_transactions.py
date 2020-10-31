class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        """Array.

        Running time: O(n^2) where n == len(transactions).
        """
        t = collections.defaultdict(list)
        for transaction in transactions:
            tx = transaction.split(',')
            t[tx[0]].append([int(tx[1]), int(tx[2]), tx[3]])
        res = []
        for k, v in t.items():
            v = sorted(v, key=lambda x: x[0])
            times = [i[0] for i in v]
            for i in range(len(v)):
                if v[i][1] > 1000:
                    res.append('{},{},{},{}'.format(k, v[i][0], v[i][1], v[i][2]))
                    continue
                l = bisect.bisect_left(times, v[i][0] - 60)
                r = bisect.bisect_right(times, v[i][0] + 60)
                for j in range(l, r):
                    if v[j][2] != v[i][2]:
                        res.append('{},{},{},{}'.format(k, v[i][0], v[i][1], v[i][2]))
                        break
        return res
