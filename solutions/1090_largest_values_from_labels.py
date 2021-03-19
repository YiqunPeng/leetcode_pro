class Solution:
    def largestValsFromLabels(self, values: List[int], labels: List[int], num_wanted: int, use_limit: int) -> int:
        """Sort.

        Running time: O(nlogn) where n == len(values).
        """
        a = sorted([(values[i], labels[i]) for i in range(len(values))], key=lambda x: x[0])
        s = 0
        u = collections.defaultdict(int)
        res = 0
        while a and s < num_wanted:
            v, l = a.pop()
            if u[l] < use_limit:
                s += 1
                res += v
                u[l] += 1
        return res
