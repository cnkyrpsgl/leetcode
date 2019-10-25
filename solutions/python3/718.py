class Solution:
    def findLength(self, A, B):
        A, res, sub = "X%sX" % "X".join(map(str, A)), 0, "X"
        for num in B:
            sub += str(num) + "X"
            if sub in A: res += 1
            else: sub = sub[sub[1:].index("X") + 1:]
        return res