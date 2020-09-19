class Logger:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = collections.deque()
        self.msg = set()
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        """Queue.
        
        Running time: O(n) where n is the length of the queue.
        """
        while self.q and timestamp - self.q[0][0] >= 10:
            t, m = self.q.popleft()
            self.msg.discard(m)
        res = message not in self.msg
        if res:
            self.q.append([timestamp, message])
            self.msg.add(message)
        return res