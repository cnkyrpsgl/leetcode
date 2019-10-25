class Solution:
    def validMountainArray(self, A):
        i = A and A.index(max(A))
        return A and 0<i<len(A)-1 and all(a1<a2 for a1,a2 in zip(A[:i],A[1:i+1])) and all(a2>a3 for a2,a3 in zip(A[i:],A[i+1:])) or False