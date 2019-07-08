# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """Two pointers.
        
        Running Time: O(n) where n is the length of linked list.
        """
        if not head:
            return False
        
        s = f = head
        
        while f.next and f.next.next:        
            s = s.next
            f = f.next.next
            
            if s is f:
                return True
            
        return False
        