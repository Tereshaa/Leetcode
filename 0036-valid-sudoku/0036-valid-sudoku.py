class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if(board[i][j]!='.'):
                    ele = board[i][j]
                    for x in range(9):
                        if x!=j:
                            if board[i][x] == ele:
                                return False
                    for y in range(9):
                        if y != i:
                            if board[y][j] == ele:
                                return False
                    if i<3:
                        if j<3:
                            for x in range(0,3):
                                for y in range(0,3):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<6:
                            for x in range(0,3):
                                for y in range(3,6):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<9:
                            for x in range(0,3):
                                for y in range(6,9):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                    elif i<6:
                        if j<3:
                            for x in range(3,6):
                                for y in range(0,3):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<6:
                            for x in range(3,6):
                                for y in range(3,6):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<9:
                            for x in range(3,6):
                                for y in range(6,9):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                    elif i<9:
                        if j<3:
                            for x in range(6,9):
                                for y in range(0,3):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<6:
                            for x in range(6,9):
                                for y in range(3,6):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
                        elif j<9:
                            for x in range(6,9):
                                for y in range(6,9):
                                    if (x != i or y != j):
                                        if board[x][y] == ele:
                                            return False
        return True
            