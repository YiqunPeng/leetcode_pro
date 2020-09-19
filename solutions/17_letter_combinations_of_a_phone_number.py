class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """Backtracking.

        Running time: O(4^n) where n is the length of digits.
        """
        def backtracking(digits):
            if not digits:
                return []
            if len(digits) == 1:
                return list(mappings[digits[0]])
            res = []
            for c in list(mappings[digits[0]]):
                for comb in backtracking(digits[1:]):
                    res.append(c + comb)
            return res
        
        mappings = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        return backtracking(digits)