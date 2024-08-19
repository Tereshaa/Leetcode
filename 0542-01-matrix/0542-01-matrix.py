class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows=len(mat)
        cols=len(mat[0])

        dist=[[float("inf")]*cols for _ in range(rows)]
        queue=deque()
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j]==0:
                    dist[i][j]=0
                    queue.append((i,j))
        
        directions=[(1,0),(0,1),(-1,0),(0,-1)]
        
        while queue:
            x,y=queue.popleft()
            for dr,dc in directions:
                nx=dr+x
                ny=dc+y
                if 0<=nx<rows and 0<=ny<cols:
                    if dist[nx][ny]>dist[x][y]+1:
                        dist[nx][ny]=dist[x][y]+1
                        queue.append((nx,ny))
        return dist
                    
        