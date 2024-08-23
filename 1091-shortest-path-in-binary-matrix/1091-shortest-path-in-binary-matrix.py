class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n=len(grid)
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        visited=[[False]*n for _ in range(n)]
        queue=deque([(0,0,1)])
        visited[0][0]=True
        
        while queue:
            r,c,length=queue.popleft()
            if r==n-1 and c==n-1:
                return length
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if 0<=row<n and 0<=col<n and not visited[row][col] and grid[row][col]==0:
                    visited[row][col]=True
                    queue.append((row,col,length+1))
        return -1

       