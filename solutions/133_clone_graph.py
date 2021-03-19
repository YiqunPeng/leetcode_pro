class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
        t = node
        d = {}
        q = deque([node])
        v = set([node])
        while q:
            node = q.popleft()
            cnode = Node(node.val)
            d[node] = cnode
            for nei in node.neighbors:
                if nei not in v:
                    v.add(nei)
                    q.append(nei)
        for node, cnode in d.items():
            cnei = []
            for nei in node.neighbors:
                cnei.append(d[nei])
            cnode.neighbors = cnei
        return d[t]
