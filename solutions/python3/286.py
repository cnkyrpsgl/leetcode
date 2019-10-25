class Solution:
    def wallsAndGates(self, rooms):
        m, n = len(rooms), len(rooms and rooms[0])  
        q, dist = [(i, j) for i in range(m) for j in range(n) if not rooms[i][j]], 0
        while q:
            new = []
            dist += 1
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2147483647:
                        rooms[x][y] = dist
                        new.append((x, y))
            q = new