class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        mat = [['' for _ in range(3)]for _ in range(3)]
        for ind, move in enumerate(moves):
            i, j = move
            mat[i][j] = ind % 2
        for cur in range(3):
            if mat[cur][0] == mat[cur][1] == mat[cur][2] == 0:
                return 'A'
            if mat[cur][0] == mat[cur][1] == mat[cur][2] == 1:
                return 'B'
            if mat[0][cur] == mat[1][cur] == mat[2][cur] == 0:
                return 'A'
            if mat[0][cur] == mat[1][cur] == mat[2][cur] == 1:
                return 'B'
        if mat[0][0] == mat[1][1] == mat[2][2] == 0 or mat[0][2] == mat[1][1] == mat[2][0] == 0:
            return 'A'
        if mat[0][0] == mat[1][1] == mat[2][2] == 1 or mat[0][2] == mat[1][1] == mat[2][0] == 1:
            return 'B'
        if len(moves) == 9:
            return 'Draw'
        return 'Pending'
            
