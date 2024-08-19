class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        
        if not board:
            return 
        
        def dfs(r,c):
            if r<0 or c<0 or r>=rows or c>=cols or board[r][c]!="O":
                return
            board[r][c]="*"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)
            
        for i in range(rows):
            if board[i][0]=="O":
                dfs(i,0)
            if board[i][cols-1]=="O":
                dfs(i,cols-1)
        for i in range(cols):
            if board[0][i]=="O":
                dfs(0,i)
            if board[rows-1][i]=="O":
                dfs(rows-1,i)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j]=="O":
                    board[i][j]="X"
                elif board[i][j]=="*":
                    board[i][j]="O"
        
        
        