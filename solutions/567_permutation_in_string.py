class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """Sliding window.

        Running time: O(l1 + l2) where l1 == len(l1) and l2 == len(l2).
        """
        l1, l2 = len(s1), len(s2)
        if l1 > l2:
            return False
        s1_counter = Counter(s1)
        d = defaultdict(int)
        for i in range(l1):
            d[s2[i]] += 1
        if d == s1_counter:
            return True
        for i in range(l1, l2):
            d[s2[i]] += 1
            d[s2[i - l1]] -= 1
            if d[s2[i - l1]] == 0:
                d.pop(s2[i - l1])
            if d == s1_counter:
                return True
        return False
