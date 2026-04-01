class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parents = [i for i in range(n)]
        ranks = [0 for _ in range(n)]

        def find(node):
            while parents[node] != node:
                parents[node] = parents[parents[node]]
                node = parents[node]
            return parents[node]
        def union(n1, n2):
            node1, node2 = find(n1), find(n2)
            if node1 == node2:
                return False
            rank1, rank2 = ranks[node1], ranks[node2]
            if rank1 <= rank2:
                parents[node1] = node2
            elif rank1 > rank2:
                ranks[node2] += 1
            else:
                parents[node1] = node2
                ranks[node1] += 1
            return True
        unions = 0
        for edge in edges:
            a, b = edge
            if union(a, b):
                unions += 1
        return n - unions