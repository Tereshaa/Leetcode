class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        adjacencylist = defaultdict(list)
        for src, dst, curr_cost in zip(original, changed, cost):
            adjacencylist[src].append((dst, curr_cost))
       
        def dijkstra(src):
            heap = [(0, src)]
            min_cost_map = {}
            while heap:
                cost, node = heapq.heappop(heap)
                if node in min_cost_map:
                    continue
                min_cost_map[node] = cost
                for nei, neicost in adjacencylist[node]:
                    if nei not in min_cost_map:
                        heapq.heappush(heap, (cost + neicost, nei))
            return min_cost_map
     
        min_cost_maps = {}
        for c in set(source):
            min_cost_maps[c] = dijkstra(c)
        
        mincost = 0
        for src, dst in zip(source, target):
            if dst not in min_cost_maps[src]:
                return -1
            mincost += min_cost_maps[src][dst]
        
        return mincost
        