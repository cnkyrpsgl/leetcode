class Solution:
    def atMostNGivenDigitSet(self, D, N):
        def less(c):
            return len([char for char in D if char < c])
        d, cnt, l = len(D), 0, len(str(N))
        # For numbers which have less digits than N, simply len(D) ** digits_length different numbers can be created
        for i in range(1, l):
            cnt += d ** i
        """
        We should also consider edge cases where previous digits match with related digits in N. In this case, we can make a number with             previous digits + (digits less than N[i]) + D ** remaining length
        """
        for i, c in enumerate(str(N)):
            cnt += less(c) * (d ** (l - i - 1))
            if c not in D: break
            if i == l - 1: cnt += 1
        return cnt