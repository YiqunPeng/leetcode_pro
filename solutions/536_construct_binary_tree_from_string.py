class Solution:
    def str2tree(self, s: str) -> TreeNode:
        st = []
        head = None
        v = []
        for i, c in enumerate(s):
            if c == ')':
                st.pop()
            elif c != '(':
                v.append(c)
                if i + 1 == len(s) or not s[i+1].isdigit():
                    node = TreeNode(int(''.join(v)))
                    v = []
                    if not head:
                        head = node
                    else:
                        parent = st[-1]
                        if parent.left:
                            parent.right = node
                        else:
                            parent.left = node
                    st.append(node)
        return head
