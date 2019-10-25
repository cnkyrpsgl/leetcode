class Solution:
    def intervalIntersection(self, A: List[Interval], B: List[Interval]) -> List[Interval]:
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            s = max(A[i].start, B[j].start)
            e = min(A[i].end, B[j].end)
            if s <= e:
                res.append(Interval(s, e))
            if A[i].end < B[j].end:
                i += 1
            elif A[i].end == B[j].end:
                i += 1
                j += 1
            else:
                j += 1
        return res