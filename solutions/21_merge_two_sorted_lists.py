# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Recursive

        Running Time: O(n) where n is the mininum length between l1 and l2
        """
        if not l1 or not l2:
            return l1 or l2
        
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    def mergeTwoLists_2(self, l1: ListNode, l2: ListNode) -> ListNode:
        """Iterative

        Running Time: O(n) where n is the mininum length between l1 and l2
        """
        nl = nh = ListNode(None)
        
        while l1 and l2:
            if l1.val < l2.val:
                nl.next = l1
                l1 = l1.next
            else:
                nl.next = l2
                l2 = l2.next
            nl = nl.next
        
        nl.next = l1 or l2
            
        return nh.next