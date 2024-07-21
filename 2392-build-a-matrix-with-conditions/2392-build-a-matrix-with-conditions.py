class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
         def dfs(node: int, graph: Dict[int, List[int]], visited: List[int], stack: List[int]) -> bool:
            if visited[node] == -1:
                return False
            if visited[node] == 1:
                return True
            visited[node] = -1
            for neighbor in graph[node]:
                if not dfs(neighbor, graph, visited, stack):
                    return False
            visited[node] = 1 
            stack.append(node)
            return True
        
         def toposort(edges):
            graph = {i: [] for i in range(1, k + 1)}
            for u, v in edges:
                graph[u].append(v)
            
            visited = [0] * (k + 1)
            stack = []
            
            for node in range(1, k + 1):
                if visited[node] == 0:
                    if not dfs(node, graph, visited, stack):
                        return []
            return stack[::-1]
        
         row_order = toposort(rowConditions)
         col_order = toposort(colConditions)

         if not row_order or not col_order:
             return []

         valtorow = {n: i for i, n in enumerate(row_order)}
         valtocol = {n: i for i, n in enumerate(col_order)}
         res = [[0] * k for _ in range(k)]

         for num in range(1, k + 1):
             r, c = valtorow[num], valtocol[num]
             res[r][c] = num
         return res

    
    
        