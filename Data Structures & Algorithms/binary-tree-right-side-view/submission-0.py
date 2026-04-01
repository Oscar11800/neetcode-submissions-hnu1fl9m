# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root: 
            return []

        rtn = []
        queue = deque()
        queue.append(root)
        while(len(queue)):
            level_len = len(queue)
            for i in range(level_len):
                root = queue.popleft()
                if i == level_len-1:
                    rtn.append(root.val)
                if root.left:
                    queue.append(root.left)
                if root.right:
                    queue.append(root.right)
        return rtn