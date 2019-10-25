class Solution:
    def read(self, buf, n):
        idx = 0
        while True:
            buf4 = [""] * 4
            curr = min(read4(buf4), n - idx)
            for i in range(curr):
                buf[idx] = buf4[i]
                idx += 1
            if curr != 4 or idx == n:
                return idx
