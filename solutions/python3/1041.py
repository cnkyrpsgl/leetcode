class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x, y, dx, dy = 0, 0, 0, 1
        for _ in range(4):
            for ins in instructions:
                if ins == 'G':
                    x += dx
                    y += dy
                elif ins == 'L':
                    dx, dy = -dy, dx
                else:
                    dx, dy = dy, -dx
        return x == y == 0