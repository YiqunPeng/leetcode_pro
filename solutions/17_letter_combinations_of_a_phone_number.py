class Solution:

    def __init__(self):
        self.m = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        self.res = []

    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return self.res
        self.dfs(digits, '')
        return self.res
    
    def dfs(self, digits, s):
        if not digits:
            self.res.append(s)
            return 
        for v in self.m[digits[0]]:
            for c in v:
                self.dfs(digits[1:], s + c)