class Solution:
    def mirrorReflection(self, p, q):
        side, up, h = 2, 1, 0
        while True:
            h += q * up
            side = (side + 1) % 2
            if side == 0:
                side += 2
            if h < 0:
                h *= -1
                up *= -1
            elif h > p:
                h = p - (h - p)
                up *= -1
            if h % p == 0:
                return h and side or 0