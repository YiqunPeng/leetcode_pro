class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        """BFS

        Running Time: O(n!) where n is the length of s.
        """
        def is_valid(s):
            c = 0
            for i in s:
                if i == '(':
                    c += 1
                elif i == ')':
                    c -= 1
                if c < 0:
                    return False
            return c == 0
        
        lv = {s}
        while lv:
            ret = list(filter(is_valid, lv))
            if ret: return ret          
            lv = {n[:i] + n[i+1:] for n in lv for i in range(len(n))}

        return [s.replace('(', '').replace(')', '')]
        