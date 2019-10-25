class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        for i in range(1,2+len(B)//len(A)+1):
            if B in A*i: return i 
        return -1