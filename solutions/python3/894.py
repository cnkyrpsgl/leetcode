class Solution:
    def allPossibleFBT(self, N):
        def constr(N):
            if N == 1: yield TreeNode(0)
            for i in range(1, N, 2):
                for l in constr(i):
                    for r in constr(N - i - 1):
                        m = TreeNode(0)
                        m.left = l
                        m.right = r
                        yield m
        return list(constr(N))