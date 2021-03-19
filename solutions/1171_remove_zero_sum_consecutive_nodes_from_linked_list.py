class Solution:
    def removeZeroSumSublists(self, head: ListNode) -> ListNode:
        s = 0
        dummy = ListNode(0, head)
        cur = dummy
        d = OrderedDict()
        while cur:
            s += cur.val
            node = d.get(s, cur)
            while s in d:
                d.popitem()
            d[s] = node
            cur = cur.next
            node.next = cur
        return dummy.next
