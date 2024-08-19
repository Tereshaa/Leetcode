class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        def dfs(node,c):
            if color[node] != -1:
                return color[node]==c
            color[node]=c

            for neighbors in graph[node]:
                if not dfs(neighbors,1-c):
                    return False
            return True
        for i in range(len(graph)):
            if color[i]== -1:
                if not dfs(i,0):
                    return False
        return True
        
        
        
        
        
#         bfs approach
#         color=[-1]*len(graph)
        
#         def bfs(start):
#             queue=deque([start])
#             color[start]=0
#             while queue:
#                 node=queue.popleft()
#                 for neighbor in graph[node]:
#                     if color[neighbor]== -1:
#                         color[neighbor]=1-color[node]
#                         queue.append(neighbor)
#                     elif color[neighbor]==color[node]:
#                         return False
#             return True
#         for i in range(len(graph)):
#             if  color[i]== -1:
#                 if not bfs(i):
#                     return False
#         return True
        