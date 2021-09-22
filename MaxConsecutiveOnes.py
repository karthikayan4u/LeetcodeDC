class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m_window = 0
        cur_window_size = 0
        for i in nums + [0]:
            cur_window_size += i
            if i == 0:
                m_window = max(m_window, cur_window_size)
                cur_window_size = 0
        return m_window
