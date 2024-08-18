class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        queue=deque()
        rows=len(grid)
        cols=len(grid[0])
        fresh=0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c]==2:
                    queue.append((r,c,0))
                elif grid[r][c]==1:
                    fresh+=1
        mins=0
        directions=[(0,1),(1,0),(-1,0),(0,-1)]
        
        while queue:
            r,c,m=queue.popleft()
            for dr,dc in directions:
                row=dr+r
                col=dc+c
                if 0<=row<rows and 0<=col<cols and grid[row][col]==1:
                    grid[row][col]=2
                    fresh-=1
                    queue.append((row,col,m+1))
                    mins=m+1
        if fresh>0:
            return -1
        return mins

        