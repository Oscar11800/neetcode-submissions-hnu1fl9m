class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        inbound = defaultdict(int)
        edges = set()
        unique_chars = set()
        # compare adj words to create edges and inbound
        for word in words:
            for c in word:
                unique_chars.add(c)
        for i in range(len(words)-1):
            w1 = words[i]
            w2 = words[i+1]
            j = 0
            while j < len(w1) and j < len(w2):
                if w1[j] == w2[j]:
                    j += 1
                else:
                    src = w1[j]
                    dst = w2[j]
                    if (src, dst) in edges:
                        break
                    else:
                        inbound[dst] += 1
                        edges.add((src, dst))
                        break
                    
            if j == len(w2) and len(w2) < len(w1):
                return ""
        # construct adj list
        adj = {src: [] for src in unique_chars}

        for edge in edges:
            a, b = edge
            adj[a].append(b)
        # Kahn's BFS to get order
        queue = deque()
        order = []
        # init queue with earliest char(s)
        for node in unique_chars:
            if inbound[node] == 0:
                queue.append(node)

        # process chars and get order
        while queue:
            node = queue.pop()
            order.append(node)
            for neighbor in adj[node]:
                inbound[neighbor] -= 1
                if inbound[neighbor] == 0:
                    queue.append(neighbor)
        # check for cycles
        if len(order) != len(unique_chars):
            return ""
        return ''.join(order)