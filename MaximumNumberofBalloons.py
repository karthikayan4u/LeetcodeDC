class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for i in text:
            if i in words:
                words[i] += 1
        return min(words['b'], words['a'], words['l'] // 2, words['o'] // 2, words['n'])
