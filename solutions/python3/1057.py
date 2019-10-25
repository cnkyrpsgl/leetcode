class Solution:
    def assignBikes(self, W: List[List[int]], B: List[List[int]]) -> List[int]:
        ans, used = [-1] * len(W), set()
        for d, w, b in sorted([abs(W[i][0] - B[j][0]) + abs(W[i][1] - B[j][1]), i, j] for i in range(len(W)) for j in range(len(B))):
            if ans[w] == -1 and b not in used:
                ans[w] = b
                used.add(b)
            if len(used) == len(ans):
                break
        return ans