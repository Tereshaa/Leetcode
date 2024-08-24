class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = {i:[] for i in range(n)}
        for u, v, w in flights:
            graph[u].append((v, w))
            
        dp=[float("inf")]*n
        dp[src]=0
        queue=deque([(src,0)]) #current city,current cost
        
        levels=0
        while queue and levels<=k:
            current_dp=dp[:]
            for _ in range(len(queue)):
                node,curr_cost=queue.popleft()
                for v,w in graph[node]:
                    if curr_cost+w<current_dp[v]:
                        current_dp[v]=curr_cost+w
                        queue.append((v,current_dp[v]))
            dp=current_dp
            levels+=1
        return dp[dst] if dp[dst]!=float("inf") else -1
        
      