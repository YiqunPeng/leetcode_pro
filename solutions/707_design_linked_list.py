class MyLinkedListNode:
    
    def __init__(self, v=None, p=None, n=None):
        """Initialize a node in linked list.
        """
        self.val = v
        self.prev = p
        self.next = n
        

class MyLinkedList:

    def __init__(self):
        """Initialize your data structure here.

        Running Time: O(1)
        """
        self.head = MyLinkedListNode()
        self.tail = MyLinkedListNode()
        
        self.head.next = self.tail
        self.tail.prev = self.head
        
        self.size = 0
        

    def get(self, index: int) -> int:
        """Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        
        Running Time: O(size of list)
        """
        def getFromHead(m):
            p = self.head
            while m > 0:
                m -= 1
                p = p.next
            return p.next.val
        
        def getFromTail(m):
            p = self.tail
            while m > 0:
                m -= 1
                p = p.prev
            return p.prev.val
        
        if index < 0 or index >= self.size:
            return -1
        
        if index < self.size // 2:
            return getFromHead(index)
        else:
            return getFromTail(self.size - 1 - index)
        

    def addAtHead(self, val: int) -> None:
        """Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        
        Running Time: O(1)
        """
        n = MyLinkedListNode(val, self.head, self.head.next)
        
        self.head.next = n
        n.next.prev = n
        
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        """Append a node of value val to the last element of the linked list.
        
        Running Time: O(1)
        """
        n = MyLinkedListNode(val, self.tail.prev, self.tail)
        
        self.tail.prev = n
        n.prev.next = n
        
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        """Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        
        Running Time: O(size of list)
        """
        def addFromHead(m):
            p = self.head
            while m > 0:
                m -= 1
                p = p.next

            n = MyLinkedListNode(val, p, p.next)
            p.next = n
            n.next.prev = n
            
        def addFromTail(m):
            p = self.tail
            while m > 0:
                m -= 1
                p = p.prev
            
            n = MyLinkedListNode(val, p.prev, p)
            p.prev = n
            n.prev.next = n
        
        if index > self.size:
            return
        
        index = max(0, index)
        if index < self.size // 2:
            addFromHead(index)
        else:
            addFromTail(self.size - index)

        self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        """Delete the index-th node in the linked list, if the index is valid.
        
        Running Time: O(size of list)
        """
        def deleteFromHead(m):
            p = self.head
            while m > 0:
                m -= 1
                p = p.next

            p.next = p.next.next   
            p.next.prev = p
            
        def deleteFromTail(m):
            p = self.tail
            while m > 0:
                m -= 1
                p = p.prev
            
            p.prev = p.prev.prev
            p.prev.next = p
        
        if index < 0 or index >= self.size:
            return
        
        if index < self.size // 2:
            deleteFromHead(index)
        else:
            deleteFromTail(self.size - 1 - index)
   
        self.size -= 1
