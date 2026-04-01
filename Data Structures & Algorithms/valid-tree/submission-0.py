class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        # construct adj list
        adj = [[] for _ in range(n)]
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])
        # dfs
        self.visited = set()
        def dfs(node):
            self.visited.add(node)
            for neighbor in adj[node]:
                if neighbor not in self.visited:
                    dfs(neighbor)
        dfs(0)
        return len(self.visited) == n