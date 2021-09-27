class Solution:
    def movesToChessboard(self, board):
        N = len(board)
        rp, cp = board[0], [x[0] for x in board]
        rn, cn = [(x+1)%2 for x in rp], [(x+1)%2 for x in cp]
        
        def checkandreturn(is_row):
            count = errs = 0
            for i in range(N):
                if is_row: line, pos, neg = board[i], rp, rn
                else: line, pos, neg = [x[i] for x in board], cp, cn
                
                if line == pos:
                    count+=1
                    if i%2!=0: errs+=1
                elif line == neg:
                    if i%2==0: errs+=1
                else: return -1
            if not(count == N // 2 or (N%2==1 and count == (N//2) + 1)): return -1
            pos1 = math.inf if errs%2!=0 else errs//2
            pos2 = math.inf if (N-errs)%2!=0 else (N-errs)//2
            return min(pos1, pos2)
                    
        row_swaps = checkandreturn(True)
        if row_swaps == -1: return -1
        col_swaps = checkandreturn(False)
        if col_swaps == -1: return -1
        return row_swaps + col_swaps
