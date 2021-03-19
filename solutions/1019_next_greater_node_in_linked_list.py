class Solution:
    def nextLargerNodes(self, head: ListNode) -> List[int]:
        st = []
        res = []
        while head:
            while st and st[-1][1] < head.val:
                idx, v = st.pop()
                res[idx] = head.val
            st.append((len(res), head.val))
            res.append(0)
            head = head.next
        return res
