class Solution:
    def findBlackPixel(self, picture, N):
        m, n, res = len(picture), len(picture[0]), 0
        for row in picture:
            r_cnt = row.count("B")
            if r_cnt != N:
                continue
            for j in range(n):
                if row[j] == "B":
                    col_cnt = same = 0
                    for i in range(m):
                        if picture[i][j] == "B":
                            col_cnt += 1
                            if picture[i] == row:
                                same += 1 
                            else:
                                break
                    if r_cnt == col_cnt == same:
                        res += 1
        return res