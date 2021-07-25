class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        dummy = d = ListNode(0, head)
        freq = defaultdict(int)
        while d.next:
            freq[d.next.val] += 1
            d = d.next
        d = dummy
        while d.next:
            if freq[d.next.val] > 1:
                d.next = d.next.next
            else:
                d = d.next
        return dummy.next
