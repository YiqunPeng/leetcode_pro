class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        head = ListNode()
        p = head

        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heappush(heap, (lists[i].val, i))
        
        while heap:
            v, i = heappop(heap)
            node = lists[i]
            lists[i] = node.next
            if lists[i]:
                heappush(heap, (lists[i].val, i))
            p.next = node
            p = node
        
        return head.next