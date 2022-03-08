class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        h = head
        while h.next:
            if h.next.next and h.next.val == 0:
                h = h.next 
            else:
                h.val += h.next.val
                h.next = h.next.next
        return head
