class Solution:
    def printLinkedListInReverse(self, head: 'ImmutableListNode') -> None:
        st = []
        while head:
            st.append(head)
            head = head.getNext()
        while st:
            st[-1].printValue()
            st.pop()
