class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True
        graph={i:[] for i in range(n)}
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        queue=deque([source])
        visited=set([source])
        
        while queue:
            node=queue.popleft()
            for neighbors in graph[node]:
                if neighbors==destination:
                    return True
                if neighbors not in visited:
                    visited.add(neighbors)
                    queue.append(neighbors)
        return False
        