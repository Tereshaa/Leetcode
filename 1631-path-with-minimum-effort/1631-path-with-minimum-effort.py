class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows=len(heights)
        cols=len(heights[0])
        directions=[(0,1),(1,0),(0,-1),(-1,0)]
        min_efforts=[[float("inf")]*cols for _ in range(rows)]
        min_efforts[0][0]=0
        heap=[(0,0,0)]
        
        while heap:
            diff,r,c=heapq.heappop(heap)
            if r==rows-1 and c==cols-1:
                return diff
            for dr,dc in directions:
                nr=dr+r
                nc=dc+c
                if 0<=nr<rows and 0<=nc<cols:
                    new_effort=max(diff,abs(heights[nr][nc]-heights[r][c]))
                    if new_effort<min_efforts[nr][nc]:
                        min_efforts[nr][nc]=new_effort
                        heapq.heappush(heap,(new_effort,nr,nc))
        return -1

   