class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD=10**9+7
        graph={i:[] for i in range(n)}
        for u,v,time in roads:
            graph[u].append((v,time))
            graph[v].append((u,time))
        distance=[float("inf")]*n
        count=[0]*n
        distance[0]=0
        count[0]=1
        
        heap=[(0,0)]
        
        while heap:
            current_dist,node=heapq.heappop(heap)
            if current_dist>distance[node]:
                continue
            
            for neighbor,time in graph[node]:
                new_time=current_dist+time
                if new_time<distance[neighbor]:
                    distance[neighbor]=new_time
                    count[neighbor]=count[node]
                    heapq.heappush(heap,(new_time,neighbor))
                elif new_time==distance[neighbor]:
                    count[neighbor]=(count[node]+count[neighbor])%MOD
        return count[n-1]
                    