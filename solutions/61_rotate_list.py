# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        """Linked list

        Running Time: O(n) where n is the length of linked list.
        """
        if not head: return None
        
        d = p = nh = ListNode(None)
        d.next = p.next = head
        
        l = 0
        while p.next:
            l += 1
            p = p.next
        k = k % l
        
        p = d
        while k:
            p = p.next
            k -= 1
            
        while p.next:
            d = d.next
            p = p.next
            
        nh = d.next if d.next else head
        p.next = head if nh is not head else None
        d.next = None
        
        return nh
        