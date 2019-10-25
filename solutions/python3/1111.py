class Solution:
    def maxDepthAfterSplit(self, seq: str) -> List[int]:
        stack = []
        res = [0] * len(seq)
        for i, c in enumerate(seq):
            if c == '(':
                stack.append(i if not stack or stack[-1] < 0 else -i)
            else:
                ind = stack.pop()
                if ind >= 0:
                    res[i] = res[ind] = 1
        return res       