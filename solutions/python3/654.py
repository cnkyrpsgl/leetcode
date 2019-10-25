class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            pos = nums.index(max(nums))
            root = TreeNode(nums[pos])
            root.left = self.constructMaximumBinaryTree(nums[:pos])
            root.right = self.constructMaximumBinaryTree(nums[pos+1:])
            return root