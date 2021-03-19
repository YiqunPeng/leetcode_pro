class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        l = 0
        node = root
        while node:
            l += 1
            node = node.next
        d, m = divmod(l, k)
        res = []
        for i in range(m):
            res.append(root)
            for j in range(d):
                root = root.next
            nxt = root.next
            root.next = None
            root = nxt
        for i in range(k - m):
            if not root:
                res.append(None)
                continue
            res.append(root)
            for j in range(d - 1):
                root = root.next
            nxt = root.next
            root.next = None
            root = nxt
        return res
