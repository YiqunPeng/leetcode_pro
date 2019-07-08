# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head):
        """Two pointers.

        Running Time: O(length of linked list)
        """
        f, s = head, head
        
        while f.next and f.next.next:
            s = s.next
            f = f.next.next
        
        return s.next if f.next else s
    