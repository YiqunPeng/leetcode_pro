class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        if not pre:
            return None
        if len(pre) == 1:
            return TreeNode(pre[0])
        lroot = post.index(pre[1])
        l = self.constructFromPrePost(pre[1:lroot+2], post[:lroot+1])
        r = self.constructFromPrePost(pre[lroot+2:], post[lroot+1:-1])
        return TreeNode(pre[0], l, r)
