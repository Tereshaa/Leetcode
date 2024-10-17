class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = collections.defaultdict(list)  # a -> [(b, a/b)]
        
        # Build the graph
        for i, eq in enumerate(equations):
            a, b = eq
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))
        
        def bfs(src: str, target: str) -> float:
            if src not in graph or target not in graph:
                return -1.0
            
            q = deque([(src, 1.0)])  # queue stores (node, accumulated product)
            visited = set()  # keep track of visited nodes
            
            while q:
                n, w = q.popleft()
                
                if n == target:
                    return w  # return the accumulated product if target is found
                
                visited.add(n)  # Mark the node as visited
                
                for nei, weight in graph[n]:
                    if nei not in visited:
                        q.append((nei, w * weight))  # Accumulate the product of weights
            
            return -1.0  # return -1.0 if the target is not reachable
        
        # Process each query
        return [bfs(q[0], q[1]) for q in queries]