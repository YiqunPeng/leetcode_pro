class Solution:
    def simplifyPath(self, path: str) -> str:
        if not path:
            return None
        dirs = path.split('/')
        st = []
        for d in dirs:
            if d == '..':
                if st:
                    st.pop()
            elif d != '' and d != '.':
                st.append(d)
        return '/' + '/'.join(st)
