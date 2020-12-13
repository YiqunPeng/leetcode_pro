class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        """Hash table.

        Running time: O(nlogn) where n == len(keyName).
        """
        d = collections.defaultdict(list)
        for i in range(len(keyName)):
            t = int(keyTime[i][:2]) * 60 + int(keyTime[i][3:])
            d[keyName[i]].append(t)
        res = []
        for k, v in d.items():
            v = sorted(v)
            for i in range(len(v) - 2):
                if v[i+2] - v[i] <= 60:
                    res.append(k)
                    break
        return sorted(res)
