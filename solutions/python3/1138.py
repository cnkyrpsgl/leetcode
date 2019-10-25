class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        ind = {s: [i // 5, i % 5] for i, s in enumerate(string.ascii_lowercase)}
        x = y = 0
        res = ""
        for c in target:
            xx, yy = ind[c]
            if yy < y:
                res += 'L' * (y - yy)
            if xx > x:
                res += 'D' * (xx - x)
            if xx < x:
                res += 'U' * (x - xx)
            if yy > y:
                res += 'R' * (yy - y)
            res += '!'
            x, y = xx, yy
        return res