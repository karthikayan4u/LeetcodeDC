class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        total = sum(shifts)
        result = ''
        for i in range(len(shifts)):
            result += chr(97 + (ord(s[i]) - 97 + total) % 26)
            total -= shifts[i]
        return result
