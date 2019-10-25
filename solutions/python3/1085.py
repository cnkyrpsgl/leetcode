class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        return 1 - sum(map(int, str(min(A)))) % 2
        return 1 - sum(int(c) for c in str(min(A))) % 2