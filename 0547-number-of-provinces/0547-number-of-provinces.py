class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=[[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1:
                    adj[i].append(j)
        visited=[0]*len(isConnected)
        def dfs(node):
            visited[node]=1
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    dfs(neighbor)
        count=0
        for i in range(len(isConnected)):
            if not visited[i]:
                count+=1
                dfs(i)
        return count
        
        