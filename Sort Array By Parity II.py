class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        odd_pos = 1
        for even_pos in range(0, len(nums), 2):
            if nums[even_pos] % 2 != 0:
                while nums[odd_pos] % 2 != 0:
                    odd_pos += 2
                nums[even_pos], nums[odd_pos] = nums[odd_pos], nums[even_pos]
        return nums
    
        Time: O(n)
        Space: O(1)
