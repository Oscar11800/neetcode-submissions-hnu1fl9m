# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if p and not q:
            return False
        if q and not p:
            return False

        stack = [(p, q)]
        while stack:
            p_node, q_node = stack.pop()
            if p_node.val != q_node.val:
                return False
            if p_node.left:
                if not q_node.left:
                    return False
                stack.append((p_node.left, q_node.left))
            else:
                if q_node.left:
                    return False
            if p_node.right:
                if not q_node.right:
                    return False
                stack.append((p_node.right, q_node.right))
            else:
                if q_node.right:
                    return False
        return True