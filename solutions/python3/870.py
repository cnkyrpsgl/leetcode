class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort(reverse = True)
        non = []
        res = [-1] * len(A)
        for b, i in sorted([(b, i) for i, b in enumerate(B)]):
            while A and A[-1] <= b:
                non.append(A.pop())
            if A:
                res[i] = A.pop()
            else:
                break
        for i in range(len(res)):
            if res[i] == -1:
                res[i] = non.pop()
        return res 