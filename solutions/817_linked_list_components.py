class Solution:
    def numComponents(self, head: ListNode, G: List[int]) -> int:
        g = set(G)
        res = 0
        while head:
            if head.val in g and (not head.next or head.next.val not in g):
                res += 1
            head = head.next
        return res
