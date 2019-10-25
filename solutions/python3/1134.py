class Solution:
    def isArmstrong(self, N: int) -> bool:
        ns = [(int(c), int(c)) for c in str(N)]
        sm = sum(a for a, b in ns)
        while sm < N:
            ns = [(a * b, b) for a, b in ns]
            sm = sum(a for a, b in ns)
        return sm == N
        