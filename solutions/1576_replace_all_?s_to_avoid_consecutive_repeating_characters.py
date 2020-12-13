class Solution:
    def modifyString(self, s: str) -> str:
        """String.

        Running time: O(n) where n == len(s).
        """
        li = list(s)
        for i in range(len(li)):
            if li[i] == '?':
                if i == 0:
                    if len(li) > 1 and li[1] != 'a':
                        li[0] = 'a'
                    else:
                        li[0] = 'b'
                elif i == len(li) - 1:
                    if li[-2] != 'a':
                        li[-1] = 'a'
                    else:
                        li[-1] = 'b'
                else:
                    s = set([li[i-1], li[i+1]])
                    if 'a' not in s:
                        li[i] = 'a'
                    elif 'b' not in s:
                        li[i] = 'b'
                    else:
                        li[i] = 'c'
        return ''.join(li)
