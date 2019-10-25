class Solution:
    def baseNeg2(self, n: int) -> str:
        bits = []
        while n:
            n, rem = divmod(n, -2)
            if rem < 0:
                n += 1
                rem -= -2
            bits.append(str(rem))
        return "".join(bits[::-1]) if bits else '0'