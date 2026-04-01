"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        queue = deque()
        queue.append(node)
        hashmap = {}
        hashmap[node] = Node(node.val)

        while queue:
            og_node = queue.popleft()
            for neighbor in og_node.neighbors:
                
                if neighbor not in hashmap:
                    queue.append(neighbor)
                    cloned_neighbor = Node(neighbor.val)
                    hashmap[neighbor] = cloned_neighbor
                else:
                    cloned_neighbor = hashmap[neighbor]
                hashmap[og_node].neighbors.append(cloned_neighbor)

        return hashmap[node]