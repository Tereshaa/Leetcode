class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        
        # Initialize DP array with infinity
        dp = [float('inf')] * n
        dp[src] = 0
        
        # Initialize a queue for BFS
        queue = deque([(src, 0)])  # (current city, current cost)
        
        # Perform BFS up to k+1 levels
        level = 0
        while queue and level <= k:
            size = len(queue)
            current_dp = dp[:]  # Copy current DP array to update costs at this level
            
            for _ in range(size):
                u, current_cost = queue.popleft()
                
                # Explore the neighbors of the current city
                for v, w in graph[u]:
                    if current_cost + w < current_dp[v]:
                        current_dp[v] = current_cost + w
                        queue.append((v, current_dp[v]))
            
            dp = current_dp  # Update DP array after this level
            level += 1
        
        # The minimum cost to reach `dst` after at most k stops
        return dp[dst] if dp[dst] != float('inf') else -1

        
        