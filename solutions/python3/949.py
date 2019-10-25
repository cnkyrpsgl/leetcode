class Solution:
    def largestTimeFromDigits(self, A):
        h = m = -float("inf")
        for n1, n2, n3, n4 in itertools.permutations(A):
            hh, mm = n1 * 10 + n2, n3 * 10 + n4
            if 0 <= hh <= 23 and 0 <= mm <= 59 and (hh > h or hh == h and mm > m):
                h, m = hh, mm
        sh = str(h) if h > 9 else "0" + str(h)
        sm = str(m) if m > 9 else "0" + str(m)
        return 0 <= h <= 23 and 0 <= m <= 59 and sh + ":" + sm or ""