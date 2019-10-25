class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        tar = sum(A) // 3
        sm = cnt = 0
        for a in A:
            sm += a
            if sm == tar:
                sm = 0
                cnt += 1
        return cnt == 3