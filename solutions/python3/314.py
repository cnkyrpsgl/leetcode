# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def verticalOrder(self, root):
        q, arrays = root and collections.deque([(root, 0)]) or None, collections.defaultdict(list)
        while q:
            new = collections.deque()
            for node, ind in q:
                arrays[ind].append(node.val)
                if node.left:
                    new.append((node.left, ind - 1))
                if node.right:
                    new.append((node.right, ind + 1))
            q = new
        return [arr for i, arr in sorted(arrays.items())]