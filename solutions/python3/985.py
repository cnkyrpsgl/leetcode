class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        sm = sum(a for a in A if a % 2 == 0)
        for i in range(len(queries)):
            val, ind = queries[i]
            sm -= A[ind] % 2 == 0 and A[ind]
            A[ind] += val
            sm += A[ind] % 2 == 0 and A[ind]
            queries[i] = sm
        return queries