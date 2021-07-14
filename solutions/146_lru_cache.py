class Node:
    
    def __init__(self, key=None, val=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = Node()
        self.tail = Node()
        self.head.nxt = self.tail
        self.tail.pre = self.head
        
    def add_head(self, node):
        nxt = self.head.nxt
        self.head.nxt = node
        node.nxt = nxt
        nxt.pre = node
        node.pre = self.head
        
    def move_to_head(self, node):
        nxt = node.nxt
        node.pre.nxt = nxt
        nxt.pre = node.pre
        self.add_head(node)
        
    def remove_tail(self):
        pre = self.tail.pre
        self.tail.pre = pre.pre
        pre.pre.nxt = self.tail
        return pre.key

class LRUCache:

    def __init__(self, capacity: int):
        self.d = {}
        self.l = DoublyLinkedList()
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            self.l.move_to_head(self.d[key])
            return self.d[key].val
        return -1   

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            self.d[key].val = value
            self.l.move_to_head(self.d[key])
        else:
            node = Node(key, value)
            self.d[key] = node
            if len(self.d) > self.cap:
                key = self.l.remove_tail()
                self.d.pop(key)
            self.l.add_head(node)
