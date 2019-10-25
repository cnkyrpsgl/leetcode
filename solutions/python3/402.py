class Solution:
    def removeKdigits(self, num, k):
        out = []
        for digit in num:
            while k and out and out[-1] > digit:
                out.pop()
                k -= 1
            out.append(digit)
        return ''.join(out[:-k or None]).lstrip('0') or "0"