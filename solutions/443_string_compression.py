class Solution:
    def compress(self, chars: List[str]) -> int:
        """String.

        Running time: O(n) where n == len(chars).
        """
        c = 1
        l, r = 0, 1
        while r <= len(chars):
            if r == len(chars) or chars[r] != chars[r-1]:
                chars[l] = chars[r-1]
                l += 1
                if c > 1:
                    for i in str(c):
                        chars[l] = i
                        l += 1
                c = 1
            else:
                c += 1
            r += 1
        return l
