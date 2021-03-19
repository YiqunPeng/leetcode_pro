class Solution:
    def longestZigZag(self, root: TreeNode) -> int:
        return self._post_order(root)[2]
        
    def _post_order(self, root):
        if not root:
            return -1, -1, 0
        lzig, lzag, lres = self._post_order(root.left)
        rzig, rzag, rres = self._post_order(root.right)
        zig = lzag + 1
        zag = rzig + 1
        return zig, zag, max(lres, rres, zig, zag)
