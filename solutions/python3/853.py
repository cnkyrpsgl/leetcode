class Solution:
    def carFleet(self, target, position, speed):
        res, s = 0, {position[i]: speed[i] for i in range(len(position))}
        position.sort()
        while position:
            cur = position.pop()
            res += 1
            while position and (s[position[-1]] - s[cur]) * (target - cur) / s[cur] >= cur - position[-1]:
                position.pop()
        return res