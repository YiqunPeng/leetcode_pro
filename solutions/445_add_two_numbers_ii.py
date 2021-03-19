class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        st1, st2 = [], []
        while l1:
            st1.append(l1)
            l1 = l1.next
        while l2:
            st2.append(l2)
            l2 = l2.next
        nhead = ListNode()
        c = 0
        while st1 or st2:
            if st1 and st2:
                n1, n2 = st1.pop(), st2.pop()
                v = n1.val + n2.val + c
            elif st1:
                n1 = st1.pop()
                v = n1.val + c
            else:
                n2 = st2.pop()
                v = n2.val + c  
            if v > 9:
                c = 1
                v -= 10
            else:
                c = 0
            node = ListNode(v, nhead.next)
            nhead.next = node         
        if c:
            node = ListNode(1, nhead.next)
            nhead.next = node
        return nhead.next
