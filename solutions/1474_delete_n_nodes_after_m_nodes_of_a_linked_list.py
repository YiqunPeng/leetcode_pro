class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:
        node = head
        while node:
            for i in range(m - 1):
                node = node.next
                if not node:
                    break
            else:
                for i in range(n):
                    if node and node.next:
                        node.next = node.next.next
                    else:
                        break
                node = node.next
        return head
