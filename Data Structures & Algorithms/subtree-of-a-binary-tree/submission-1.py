# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def sameTree(self, root1: Optional[TreeNode], root2:Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if (root1 and not root2) or (root2 and not root1):
            return False
        if (root1.val != root2.val):
            return False
        return self.sameTree(root1.left, root2.left) and self.sameTree(root1.right, root2.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if subRoot is None:
            return True
        if root is None:
            return False

        q = deque()
        q.append(root)
        
        while(q):
            node = q.pop()
            if self.sameTree(node, subRoot):
                return True
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return False
