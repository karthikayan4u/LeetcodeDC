class Solution:
    def maxLength(self, arr: List[str]) -> int:
        def recurse(s, ind, m):
            if len(set(s)) == len(s):
                m = max(m, len(s))
            if ind < len(arr):
                m = recurse(s + arr[ind], ind+1, m) #un iq 4
                m = recurse(s, ind+1, m) #un ue
            return m
        return recurse('', 0, 0)
