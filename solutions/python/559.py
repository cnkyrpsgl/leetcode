class Solution(object):
    def maxDepth(self, root, level = 1):
        return max(root and [self.maxDepth(child, level + 1) for child in root.children] + [level] or [0])