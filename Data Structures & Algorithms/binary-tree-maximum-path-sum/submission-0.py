# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = root.val
        def dfs(node):
            if node is None:
                return 0
            left = max(0, dfs(node.left))
            right = max(0, dfs(node.right))
            self.max_sum = max(self.max_sum, node.val + left + right)
            return max(node.val, node.val + left, node.val + right)
        dfs(root)
        return self.max_sum