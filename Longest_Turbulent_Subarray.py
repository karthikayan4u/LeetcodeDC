class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 1
        start = 0
        def compare(a, b):
            if a > b:
                return 1
            elif a < b:
                return -1
            return 0
        for i in range(1, len(arr)):
            cur = compare(arr[i-1], arr[i])
            if cur == 0:
                start = i
            elif i == len(arr) - 1 or compare(arr[i], arr[i+1]) + cur != 0:
                ans = max(ans, i - start + 1)
                start = i
        return ans
