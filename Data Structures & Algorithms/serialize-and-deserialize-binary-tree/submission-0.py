# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root: Optional[TreeNode]) -> str:
        rtn = []
        def dfs(node):
            if not node:
                rtn.append("#,")
                return
            rtn.append(f"{node.val},")
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ''.join(rtn)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        self.counter = 0
        vals = data.split(",")[:-1]
        def dfs():
            if vals[self.counter] == '#':
                self.counter += 1
                return None
            node = TreeNode(int((vals[self.counter])))
            self.counter += 1
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()
