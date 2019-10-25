class Solution:
    def robotSim(self, commands, obstacles):
        i = j = mx = 0
        d, move, obstacles = 3, [(-1, 0), (0, -1), (1, 0), (0, 1)], set(map(tuple, obstacles))
        for command in commands:
            if command == -2: d = (d + 1) % 4
            elif command == -1: d = (d - 1) % 4
            else:
                x, y = move[d]
                while command and (i + x, j + y) not in obstacles:
                    i += x
                    j += y
                    command -= 1
            mx = max(mx, i ** 2 + j ** 2)
        return mx