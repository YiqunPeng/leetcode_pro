class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        if not S: 
            return ""
        
        ans = ""
        stack = []
        
        for i, s in enumerate(S):
            if s == '(':
                stack.append((i, s))
            else:
                if stack[-1][1] == '(':
                    if len(stack) == 1:
                        ans += S[stack[0][0]+1:i]
                    stack.pop()
                else:
                    stack.append((i, s))
                    
        return ans
