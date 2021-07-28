class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """BFS

        Running Time: O(n * 2^n) where n is the length of s.
        """
        res = []
        lvl = set([s])
        while lvl:
            nlvl = set()
            for sstr in lvl:
                if self._is_valid(sstr):
                    res.append(sstr)
            if res:
                return res
            for sstr in lvl:
                for i in range(len(sstr)):
                    if sstr[i] not in [')', '(']:
                        continue
                    nlvl.add(sstr[:i] + sstr[i+1:])
            lvl = nlvl
        return res  
    
    def _is_valid(self, a):
        l = 0
        for c in a:
            if c == '(':
                l += 1
            elif c == ')':
                l -= 1
                if l < 0:
                    return False
        return l == 0
        