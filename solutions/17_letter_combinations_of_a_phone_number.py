class Solution:
    
    def __init__(self):
        self.map = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        self.res = []
    
    def letterCombinations(self, digits: str) -> List[str]:
        self._dfs(digits, 0, [])
        return self.res
    
    def _dfs(self, digits, pos, rep):
        if pos == len(digits):
            if rep:
                self.res.append(''.join(rep))
            return
        for c in self.map[digits[pos]]:
            self._dfs(digits, pos + 1, rep + [c])
