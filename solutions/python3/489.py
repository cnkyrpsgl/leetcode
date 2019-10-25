class Solution:
    def cleanRoom(self, robot, move = [(-1, 0), (0, -1), (1, 0), (0, 1)]):
        def dfs(i, j, cleaned, ind):
            robot.clean()
            cleaned.add((i, j))
            k = 0
            for x, y in move[ind:] + move[:ind]:
                if (i + x, j + y) not in cleaned and robot.move():
                    dfs(i + x, j + y, cleaned, (ind + k) % 4)
                    robot.turnLeft()
                    robot.turnLeft()
                    robot.move()
                    robot.turnRight()
                    robot.turnRight()
                robot.turnLeft()
                k += 1
        dfs(0, 0, set(), 0) 