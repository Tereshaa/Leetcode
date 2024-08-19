class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        def dfs(node):
            if visited[node]!=0:
                return visited[node]==2
            
            visited[node]=1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            visited[node]=2
            return True
    
        visited=[0]*len(graph)
        safe_nodes=[]
        for i in range(len(graph)):
            if dfs(i):
                safe_nodes.append(i)
        return safe_nodes
                
        