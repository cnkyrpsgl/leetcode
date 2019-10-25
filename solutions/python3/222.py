class Solution:
    
    def countNodes(self, root):
        if not root: return 0
        l = self.getDepth(root.left)
        r = self.getDepth(root.right)
        if l == r:
            return (1 << l) + self.countNodes(root.right)
        return (1 << r) + self.countNodes(root.left)
    
    def getDepth(self, root):
        if not root: return 0
        return 1 + self.getDepth(root.left)