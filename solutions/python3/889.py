class Solution:
    def constructFromPrePost(self, pre, post):
        if pre:
            root = TreeNode(pre.pop(0))
            post.pop()
            if pre:
                if pre[0] == post[-1]:
                    root.left = self.constructFromPrePost(pre, post)
                else:
                    l, r = post.index(pre[0]), pre.index(post[-1])
                    root.left = self.constructFromPrePost(pre[:r], post[:l + 1])
                    root.right = self.constructFromPrePost(pre[r:], post[l + 1:]) 
            return root