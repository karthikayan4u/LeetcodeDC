class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        zeroes = {tuple(i) for i in mines}
        dp = [[0 for _ in range(n)] for _ in range(n)]
        answer = 0
        for r in range(n):
            co = 0
            for c in range(n):
                if (r, c) in zeroes:
                    co = 0
                else:
                    co += 1
                dp[r][c] = co
            co = 0
            for c in reversed(range(n)):
                if (r, c) in zeroes:
                    co = 0
                else:
                    co += 1
                dp[r][c] = min(dp[r][c], co)
        for c in range(n):
            co = 0
            for r in range(n):
                if (r, c) in zeroes:
                    co = 0
                else:
                    co += 1
                dp[r][c] = min(dp[r][c], co)
            co = 0
            for r in reversed(range(n)):
                if (r, c) in zeroes:
                    co = 0
                else:
                    co += 1
                dp[r][c] = min(dp[r][c], co)
                answer = max(dp[r][c], answer)
        return answer
