class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        key = keysPressed[0]
        time = releaseTimes[0]
        for i in range(1, len(keysPressed)):
            if time <= releaseTimes[i] - releaseTimes[i-1]:
                if time < releaseTimes[i] - releaseTimes[i-1] or key <keysPressed[i]:
                    key = keysPressed[i]
                time = releaseTimes[i] - releaseTimes[i-1]
        return key
