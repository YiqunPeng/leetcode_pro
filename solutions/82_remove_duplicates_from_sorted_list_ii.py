# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """Linked list.

        Running Time: O(n) where n is the length of linked list.
        """
        p = nh = ListNode(None)
        p.next = nh.next = head
        
        while p.next:
            if p.next.next and p.next.next.val == p.next.val:
                while p.next.next and p.next.next.val == p.next.val:
                    p.next = p.next.next
                p.next = p.next.next
            else:
                p = p.next
                    
        return nh.next
  