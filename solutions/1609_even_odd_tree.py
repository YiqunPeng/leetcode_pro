class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        nodes = [root]
        lvl = 0
        while nodes:
            nxt = []
            if lvl % 2 == 0:
                for i in range(len(nodes)):
                    if nodes[i].val % 2 == 0 or (i and nodes[i].val <= nodes[i-1].val):
                        return False
            else:
                for i in range(len(nodes)):
                    if nodes[i].val % 2 == 1 or (i and nodes[i].val >= nodes[i-1].val):
                        return False
            for i in range(len(nodes)):
                if nodes[i].left:
                    nxt.append(nodes[i].left)
                if nodes[i].right:
                    nxt.append(nodes[i].right)
            nodes = nxt
            lvl += 1
        return True
