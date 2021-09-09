class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        count = 0
        def nesting(ind, seq_length):
            nex, nums[ind] = nums[ind], -1
            if nex < 0:
                return seq_length
            return nesting(nex, seq_length + 1)
        for i in nums:
            if i >= 0:
                count = max(count, nesting(i, 0))
        return count
