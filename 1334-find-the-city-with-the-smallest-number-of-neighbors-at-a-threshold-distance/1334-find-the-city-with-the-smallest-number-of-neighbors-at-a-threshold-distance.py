class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][j] > dist[i][k] + dist[k][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        min_neighbor_count = float('inf')
        result_city = -1

        for i in range(n):
            neighbor_count = sum(1 for j in range(n) if dist[i][j] <= distanceThreshold)
            if neighbor_count < min_neighbor_count or (neighbor_count == min_neighbor_count and i > result_city):
                min_neighbor_count = neighbor_count
                result_city = i

        return result_city
