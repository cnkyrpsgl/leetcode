class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        num = 0
        for i in range(len(A)):
            num = (num << 1) + A[i]
            A[i] = num % 5 == 0
        return A