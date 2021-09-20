class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp = [0 for _ in range(len(t))]
        for i in range(len(s)):
            prev = 1
            for j in range(len(t)):
                temp = dp[j]
                dp[j] += prev * (s[i] == t[j])
                prev = temp
        return dp[-1]
