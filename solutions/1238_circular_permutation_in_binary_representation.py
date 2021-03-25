class Solution:
    def circularPermutation(self, n: int, start: int) -> List[int]:
        gray_codes = [0, 1]
        for i in range(1, n):
            ref = [(j + (1 << i)) for j in reversed(gray_codes)]
            gray_codes = ref + gray_codes
        for i in range(len(gray_codes)):
            if gray_codes[i] == start:
                return gray_codes[i:] + gray_codes[:i]
