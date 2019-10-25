class Solution:
    def recoverTree(self, root):
        def inorder(node):
            if node.left:
                yield from inorder(node.left)
            yield node
            if node.right:
                yield from inorder(node.right)
        swap1 = swap2 = smaller = None
        for node in inorder(root):   
            if smaller and smaller.val > node.val:
                if not swap1:  
                    swap1 = smaller
                swap2 = node      
            smaller = node
        if swap1:
            swap1.val, swap2.val = swap2.val, swap1.val