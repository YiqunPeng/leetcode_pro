class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None
        if len(lists) == 1:
            return lists[0]
        return self.merge_two(self.mergeKLists(lists[:len(lists)//2]), self.mergeKLists(lists[len(lists)//2:]))
    
    def merge_two(self, l1, l2):
        if not (l1 and l2):
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.merge_two(l1.next, l2)
            return l1
        else:
            l2.next = self.merge_two(l1, l2.next)
            return l2
